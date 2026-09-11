from django.contrib.auth import get_user_model
from django.test import TestCase

from learning.models import (
    Course,
    CourseRelease,
    Enrollment,
    Lesson,
    LessonProgress,
    Module,
)


class ProgressApiTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.learner = User.objects.create_user(
            username="api-learner",
            password="test-only-password",
        )

        self.course = Course.objects.create(
            slug="progress-course",
            subject="Backend Engineering",
            title="Progress Course",
            summary="Compatibility summary.",
            level="Foundation",
            audience="Learners",
            outcomes="Persist progress.",
            is_active=True,
        )

        self.release_one, self.lessons_one = self.create_release(
            1,
            published=True,
        )

    def create_release(self, release_number, *, published):
        release = CourseRelease.objects.create(
            course=self.course,
            release_number=release_number,
            title=f"Progress Release {release_number}",
            summary="Progress release.",
            level="Foundation",
            audience="Learners",
            outcomes="Complete lessons.",
        )

        module = Module.objects.create(
            release=release,
            position=1,
            title="Module 1",
        )

        lessons = [
            Lesson.objects.create(
                module=module,
                position=position,
                slug=f"lesson-{release_number}-{position}",
                eyebrow=f"LESSON {position}",
                title=f"Lesson {release_number}.{position}",
                summary="Lesson summary.",
                duration_minutes=10,
            )
            for position in (1, 2)
        ]

        if published:
            release.is_published = True
            release.save()

        return release, lessons

    def enroll(self):
        self.client.force_login(self.learner)
        return self.client.post(
            "/api/v1/courses/progress-course/enrollment/"
        )

    def test_progress_endpoints_require_authentication(self):
        enrollment = self.client.post(
            "/api/v1/courses/progress-course/enrollment/"
        )
        progress = self.client.get(
            "/api/v1/courses/progress-course/progress/"
        )
        completion = self.client.post(
            (
                "/api/v1/courses/progress-course/lessons/"
                f"{self.lessons_one[0].id}/complete/"
            )
        )

        self.assertEqual(enrollment.status_code, 401)
        self.assertEqual(progress.status_code, 401)
        self.assertEqual(completion.status_code, 401)

    def test_enrollment_is_idempotent(self):
        first = self.enroll()
        second = self.client.post(
            "/api/v1/courses/progress-course/enrollment/"
        )

        self.assertEqual(first.status_code, 201)
        self.assertTrue(first.json()["created"])
        self.assertEqual(second.status_code, 200)
        self.assertFalse(second.json()["created"])
        self.assertEqual(Enrollment.objects.count(), 1)

    def test_progress_requires_enrollment(self):
        self.client.force_login(self.learner)

        response = self.client.get(
            "/api/v1/courses/progress-course/progress/"
        )

        self.assertEqual(response.status_code, 404)

    def test_new_enrollment_starts_with_zero_progress(self):
        response = self.enroll()
        progress = response.json()["progress"]

        self.assertEqual(progress["release"], 1)
        self.assertEqual(progress["completedItemIds"], [])
        self.assertEqual(progress["completedItems"], 0)
        self.assertEqual(progress["totalItems"], 2)
        self.assertEqual(progress["progressPercent"], 0)
        self.assertEqual(
            progress["currentItemId"],
            str(self.lessons_one[0].id),
        )

    def test_completion_persists_and_advances_resume(self):
        self.enroll()

        response = self.client.post(
            (
                "/api/v1/courses/progress-course/lessons/"
                f"{self.lessons_one[0].id}/complete/"
            )
        )

        self.assertEqual(response.status_code, 201)

        progress = response.json()["progress"]

        self.assertEqual(
            progress["completedItemIds"],
            [str(self.lessons_one[0].id)],
        )
        self.assertEqual(progress["completedItems"], 1)
        self.assertEqual(progress["totalItems"], 2)
        self.assertEqual(progress["progressPercent"], 50)
        self.assertEqual(
            progress["currentItemId"],
            str(self.lessons_one[1].id),
        )
        self.assertEqual(LessonProgress.objects.count(), 1)

        persisted = self.client.get(
            "/api/v1/courses/progress-course/progress/"
        )

        self.assertEqual(
            persisted.json()["progress"]["progressPercent"],
            50,
        )

    def test_completion_is_idempotent(self):
        self.enroll()

        url = (
            "/api/v1/courses/progress-course/lessons/"
            f"{self.lessons_one[0].id}/complete/"
        )

        first = self.client.post(url)
        second = self.client.post(url)

        self.assertEqual(first.status_code, 201)
        self.assertEqual(second.status_code, 200)
        self.assertTrue(first.json()["created"])
        self.assertFalse(second.json()["created"])
        self.assertEqual(LessonProgress.objects.count(), 1)

    def test_progress_stays_pinned_to_enrolled_release(self):
        self.enroll()

        release_two, _ = self.create_release(
            2,
            published=True,
        )

        response = self.client.get(
            "/api/v1/courses/progress-course/progress/"
        )

        progress = response.json()["progress"]

        self.assertEqual(
            progress["releaseId"],
            str(self.release_one.id),
        )
        self.assertEqual(progress["release"], 1)
        self.assertNotEqual(
            progress["releaseId"],
            str(release_two.id),
        )

    def test_cannot_complete_lesson_from_other_release(self):
        self.enroll()

        _, lessons_two = self.create_release(
            2,
            published=True,
        )

        response = self.client.post(
            (
                "/api/v1/courses/progress-course/lessons/"
                f"{lessons_two[0].id}/complete/"
            )
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(LessonProgress.objects.count(), 0)

    def test_my_learning_requires_authentication(self):
        response = self.client.get("/api/v1/my-learning/")

        self.assertEqual(response.status_code, 401)

    def test_my_learning_returns_persisted_progress_and_current_lesson(self):
        self.enroll()

        completion = self.client.post(
            (
                "/api/v1/courses/progress-course/lessons/"
                f"{self.lessons_one[0].id}/complete/"
            )
        )
        self.assertEqual(completion.status_code, 201)

        response = self.client.get("/api/v1/my-learning/")

        self.assertEqual(response.status_code, 200)

        courses = response.json()["courses"]
        self.assertEqual(len(courses), 1)

        course = courses[0]

        self.assertEqual(course["courseSlug"], "progress-course")
        self.assertEqual(
            course["releaseId"],
            str(self.release_one.id),
        )
        self.assertEqual(course["release"], 1)

        self.assertEqual(
            course["progress"]["completedItems"],
            1,
        )
        self.assertEqual(
            course["progress"]["totalItems"],
            2,
        )
        self.assertEqual(
            course["progress"]["progressPercent"],
            50,
        )
        self.assertEqual(
            course["progress"]["currentItemId"],
            str(self.lessons_one[1].id),
        )

        self.assertEqual(
            course["current"]["itemId"],
            str(self.lessons_one[1].id),
        )
        self.assertEqual(
            course["current"]["itemTitle"],
            self.lessons_one[1].title,
        )
        self.assertEqual(
            course["current"]["moduleTitle"],
            "Module 1",
        )

    def test_my_learning_keeps_latest_enrollment_per_course(self):
        self.enroll()

        release_two, lessons_two = self.create_release(
            2,
            published=True,
        )

        Enrollment.objects.create(
            learner=self.learner,
            course_release=release_two,
        )

        response = self.client.get("/api/v1/my-learning/")

        self.assertEqual(response.status_code, 200)

        courses = response.json()["courses"]
        self.assertEqual(len(courses), 1)

        course = courses[0]

        self.assertEqual(
            course["releaseId"],
            str(release_two.id),
        )
        self.assertEqual(course["release"], 2)
        self.assertEqual(
            course["progress"]["currentItemId"],
            str(lessons_two[0].id),
        )

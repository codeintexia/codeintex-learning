from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase

from learning.models import (
    Course,
    CourseRelease,
    Enrollment,
    Lesson,
    LessonProgress,
    Module,
)


class LearningRuntimeModelTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.learner = User.objects.create_user(
            username="learner",
            password="test-only-password",
        )

        self.course = Course.objects.create(
            slug="runtime-course",
            subject="Backend Engineering",
            title="Runtime Course",
            summary="Compatibility summary.",
            level="Foundation",
            audience="Learners",
            outcomes="Understand runtime state.",
            is_active=True,
        )

    def create_release(self, release_number, *, published):
        release = CourseRelease.objects.create(
            course=self.course,
            release_number=release_number,
            title=f"Runtime Release {release_number}",
            summary="Runtime release.",
            level="Foundation",
            audience="Learners",
            outcomes="Complete lessons.",
        )

        module = Module.objects.create(
            release=release,
            position=1,
            title="Module 1",
        )

        lesson = Lesson.objects.create(
            module=module,
            position=1,
            slug=f"lesson-{release_number}",
            eyebrow="MODULE 01 · LESSON 01",
            title=f"Lesson {release_number}",
            summary="Lesson summary.",
            duration_minutes=10,
        )

        if published:
            release.is_published = True
            release.save()

        return release, lesson

    def test_enrollment_requires_published_release(self):
        release, _ = self.create_release(1, published=False)

        with self.assertRaises(ValidationError):
            Enrollment.objects.create(
                learner=self.learner,
                course_release=release,
            )

    def test_learner_can_enroll_in_published_release(self):
        release, _ = self.create_release(1, published=True)

        enrollment = Enrollment.objects.create(
            learner=self.learner,
            course_release=release,
        )

        self.assertEqual(enrollment.learner, self.learner)
        self.assertEqual(enrollment.course_release, release)

    def test_enrollment_is_unique_per_learner_and_release(self):
        release, _ = self.create_release(1, published=True)

        Enrollment.objects.create(
            learner=self.learner,
            course_release=release,
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Enrollment.objects.create(
                    learner=self.learner,
                    course_release=release,
                )

    def test_lesson_progress_can_complete_lesson_in_same_release(self):
        release, lesson = self.create_release(1, published=True)

        enrollment = Enrollment.objects.create(
            learner=self.learner,
            course_release=release,
        )

        progress = LessonProgress.objects.create(
            enrollment=enrollment,
            lesson=lesson,
        )

        self.assertEqual(progress.lesson, lesson)
        self.assertIsNotNone(progress.completed_at)

    def test_lesson_progress_rejects_lesson_from_other_release(self):
        release_one, _ = self.create_release(1, published=True)
        _, lesson_two = self.create_release(2, published=True)

        enrollment = Enrollment.objects.create(
            learner=self.learner,
            course_release=release_one,
        )

        with self.assertRaises(ValidationError):
            LessonProgress.objects.create(
                enrollment=enrollment,
                lesson=lesson_two,
            )

    def test_lesson_completion_is_unique_per_enrollment(self):
        release, lesson = self.create_release(1, published=True)

        enrollment = Enrollment.objects.create(
            learner=self.learner,
            course_release=release,
        )

        LessonProgress.objects.create(
            enrollment=enrollment,
            lesson=lesson,
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                LessonProgress.objects.create(
                    enrollment=enrollment,
                    lesson=lesson,
                )

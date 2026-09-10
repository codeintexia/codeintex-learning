from django.test import TestCase

from learning.immutability import PublishedReleaseMutationError
from learning.models import Course, CourseRelease, Lesson, Module


class PublishedReleaseImmutabilityTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            slug="test-course",
            subject="TEST",
            title="Test Course",
            summary="Compatibility summary",
            level="Foundation",
            audience="Test learners",
            outcomes="Outcome one",
        )

        self.release = CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Test Course",
            summary="Release summary",
            level="Foundation",
            audience="Test learners",
            outcomes="Outcome one",
        )

        self.module = Module.objects.create(
            release=self.release,
            position=1,
            title="Module 1",
        )

        self.lesson = Lesson.objects.create(
            module=self.module,
            position=1,
            slug="lesson-1",
            title="Lesson 1",
            summary="Lesson summary",
            duration_minutes=10,
        )

        self.release.is_published = True
        self.release.save(
            update_fields=[
                "is_published",
                "updated_at",
            ]
        )

    def test_draft_release_can_be_edited(self):
        draft = CourseRelease.objects.create(
            course=self.course,
            release_number=2,
            title="Draft",
        )

        draft.title = "Updated Draft"
        draft.save()

        draft.refresh_from_db()
        self.assertEqual(draft.title, "Updated Draft")

    def test_published_release_cannot_be_edited(self):
        self.release.title = "Mutated"

        with self.assertRaises(PublishedReleaseMutationError):
            self.release.save()

    def test_published_release_cannot_be_unpublished(self):
        self.release.is_published = False

        with self.assertRaises(PublishedReleaseMutationError):
            self.release.save()

    def test_published_release_cannot_be_deleted(self):
        with self.assertRaises(PublishedReleaseMutationError):
            self.release.delete()

    def test_course_with_published_release_cannot_be_deleted(self):
        with self.assertRaises(PublishedReleaseMutationError):
            self.course.delete()

    def test_module_cannot_be_created_in_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            Module.objects.create(
                release=self.release,
                position=2,
                title="Forbidden Module",
            )

    def test_module_in_published_release_cannot_be_edited(self):
        self.module.title = "Mutated"

        with self.assertRaises(PublishedReleaseMutationError):
            self.module.save()

    def test_module_in_published_release_cannot_be_deleted(self):
        with self.assertRaises(PublishedReleaseMutationError):
            self.module.delete()

    def test_lesson_cannot_be_created_in_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            Lesson.objects.create(
                module=self.module,
                position=2,
                slug="forbidden-lesson",
                title="Forbidden Lesson",
            )

    def test_lesson_in_published_release_cannot_be_edited(self):
        self.lesson.title = "Mutated"

        with self.assertRaises(PublishedReleaseMutationError):
            self.lesson.save()

    def test_lesson_in_published_release_cannot_be_deleted(self):
        with self.assertRaises(PublishedReleaseMutationError):
            self.lesson.delete()

    def test_bulk_release_update_cannot_mutate_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            CourseRelease.objects.filter(
                pk=self.release.pk
            ).update(title="Bulk Mutation")

    def test_bulk_release_delete_cannot_remove_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            CourseRelease.objects.filter(
                pk=self.release.pk
            ).delete()

    def test_bulk_module_update_cannot_mutate_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            Module.objects.filter(
                pk=self.module.pk
            ).update(title="Bulk Mutation")

    def test_bulk_module_delete_cannot_mutate_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            Module.objects.filter(
                pk=self.module.pk
            ).delete()

    def test_bulk_lesson_update_cannot_mutate_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            Lesson.objects.filter(
                pk=self.lesson.pk
            ).update(title="Bulk Mutation")

    def test_bulk_lesson_delete_cannot_mutate_published_release(self):
        with self.assertRaises(PublishedReleaseMutationError):
            Lesson.objects.filter(
                pk=self.lesson.pk
            ).delete()

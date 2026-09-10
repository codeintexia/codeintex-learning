import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet

from .blocks import LessonSectionBlock
from .immutability import (
    CourseReleaseQuerySet,
    LessonQuerySet,
    ModuleQuerySet,
    PublishedReleaseMutationError,
)


@register_snippet
class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    slug = models.SlugField(
        max_length=160,
        unique=True,
    )
    subject = models.CharField(
        max_length=120,
    )
    title = models.CharField(
        max_length=255,
    )
    summary = models.TextField()
    level = models.CharField(
        max_length=80,
        default="Foundation",
    )
    audience = models.TextField(
        blank=True,
    )
    outcomes = models.TextField(
        blank=True,
        help_text="One learning outcome per line.",
    )
    is_active = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    panels = [
        FieldPanel("slug"),
        FieldPanel("subject"),
        FieldPanel("title"),
        FieldPanel("is_active"),
    ]

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    @property
    def outcome_list(self):
        return [
            line.strip()
            for line in self.outcomes.splitlines()
            if line.strip()
        ]

    def delete(self, *args, **kwargs):
        if self.releases.filter(is_published=True).exists():
            raise PublishedReleaseMutationError()

        return super().delete(*args, **kwargs)


@register_snippet
class CourseRelease(models.Model):
    objects = CourseReleaseQuerySet.as_manager()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="releases",
    )
    release_number = models.PositiveIntegerField()
    title = models.CharField(
        max_length=255,
    )
    summary = models.TextField(
        blank=True,
    )
    level = models.CharField(
        max_length=80,
        default="Foundation",
    )
    audience = models.TextField(
        blank=True,
    )
    outcomes = models.TextField(
        blank=True,
        help_text="One learning outcome per line.",
    )
    is_published = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    panels = [
        FieldPanel("course"),
        FieldPanel("release_number"),
        FieldPanel("title"),
        FieldPanel("summary"),
        FieldPanel("level"),
        FieldPanel("audience"),
        FieldPanel("outcomes"),
        FieldPanel("is_published"),
    ]

    class Meta:
        ordering = ["course", "-release_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["course", "release_number"],
                name="unique_course_release_number",
            ),
        ]

    def __str__(self):
        return f"{self.course.title} · Release {self.release_number}"

    @property
    def outcome_list(self):
        return [
            line.strip()
            for line in self.outcomes.splitlines()
            if line.strip()
        ]

    def save(self, *args, **kwargs):
        if (
            not self._state.adding
            and type(self).objects.filter(
                pk=self.pk,
                is_published=True,
            ).exists()
        ):
            raise PublishedReleaseMutationError()

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if (
            self.pk
            and type(self).objects.filter(
                pk=self.pk,
                is_published=True,
            ).exists()
        ):
            raise PublishedReleaseMutationError()

        return super().delete(*args, **kwargs)


@register_snippet
class Module(models.Model):
    objects = ModuleQuerySet.as_manager()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    release = models.ForeignKey(
        CourseRelease,
        on_delete=models.CASCADE,
        related_name="modules",
    )
    position = models.PositiveSmallIntegerField()
    title = models.CharField(
        max_length=255,
    )

    panels = [
        FieldPanel("release"),
        FieldPanel("position"),
        FieldPanel("title"),
    ]

    class Meta:
        ordering = ["position"]
        constraints = [
            models.UniqueConstraint(
                fields=["release", "position"],
                name="unique_module_position_per_release",
            ),
        ]

    def __str__(self):
        return f"{self.position}. {self.title}"

    def save(self, *args, **kwargs):
        source_is_published = (
            not self._state.adding
            and type(self).objects.filter(
                pk=self.pk,
                release__is_published=True,
            ).exists()
        )

        target_is_published = (
            self.release_id
            and CourseRelease.objects.filter(
                pk=self.release_id,
                is_published=True,
            ).exists()
        )

        if source_is_published or target_is_published:
            raise PublishedReleaseMutationError()

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if (
            self.pk
            and type(self).objects.filter(
                pk=self.pk,
                release__is_published=True,
            ).exists()
        ):
            raise PublishedReleaseMutationError()

        return super().delete(*args, **kwargs)


@register_snippet
class Lesson(models.Model):
    objects = LessonQuerySet.as_manager()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    position = models.PositiveSmallIntegerField()
    slug = models.SlugField(
        max_length=160,
    )
    eyebrow = models.CharField(
        max_length=120,
        blank=True,
    )
    title = models.CharField(
        max_length=255,
    )
    summary = models.TextField(
        blank=True,
    )
    duration_minutes = models.PositiveSmallIntegerField(
        default=0,
    )
    sections = StreamField(
        [
            ("section", LessonSectionBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    panels = [
        FieldPanel("module"),
        FieldPanel("position"),
        FieldPanel("slug"),
        FieldPanel("eyebrow"),
        FieldPanel("title"),
        FieldPanel("summary"),
        FieldPanel("duration_minutes"),
        FieldPanel("sections"),
    ]

    class Meta:
        ordering = ["position"]
        constraints = [
            models.UniqueConstraint(
                fields=["module", "position"],
                name="unique_lesson_position_per_module",
            ),
            models.UniqueConstraint(
                fields=["module", "slug"],
                name="unique_lesson_slug_per_module",
            ),
        ]

    def __str__(self):
        return f"{self.position}. {self.title}"

    def save(self, *args, **kwargs):
        source_is_published = (
            not self._state.adding
            and type(self).objects.filter(
                pk=self.pk,
                module__release__is_published=True,
            ).exists()
        )

        target_is_published = (
            self.module_id
            and Module.objects.filter(
                pk=self.module_id,
                release__is_published=True,
            ).exists()
        )

        if source_is_published or target_is_published:
            raise PublishedReleaseMutationError()

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if (
            self.pk
            and type(self).objects.filter(
                pk=self.pk,
                module__release__is_published=True,
            ).exists()
        ):
            raise PublishedReleaseMutationError()

        return super().delete(*args, **kwargs)

class Enrollment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    learner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="learning_enrollments",
    )
    course_release = models.ForeignKey(
        CourseRelease,
        on_delete=models.PROTECT,
        related_name="enrollments",
    )
    enrolled_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-enrolled_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["learner", "course_release"],
                name="unique_learner_course_release_enrollment",
            ),
        ]

    def __str__(self):
        return (
            f"{self.learner} · "
            f"{self.course_release.course.title} · "
            f"Release {self.course_release.release_number}"
        )

    def clean(self):
        super().clean()

        if not self.course_release_id:
            return

        is_published = CourseRelease.objects.filter(
            pk=self.course_release_id,
            is_published=True,
        ).exists()

        if not is_published:
            raise ValidationError(
                {
                    "course_release": (
                        "Enrollment requires a published course release."
                    ),
                }
            )

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)


class LessonProgress(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="lesson_progress",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        related_name="progress_records",
    )
    completed_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["completed_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["enrollment", "lesson"],
                name="unique_lesson_progress_per_enrollment",
            ),
        ]

    def __str__(self):
        return f"{self.enrollment} · {self.lesson.title}"

    def clean(self):
        super().clean()

        if not self.enrollment_id or not self.lesson_id:
            return

        enrollment_release_id = (
            Enrollment.objects
            .filter(pk=self.enrollment_id)
            .values_list("course_release_id", flat=True)
            .first()
        )

        lesson_release_id = (
            Lesson.objects
            .filter(pk=self.lesson_id)
            .values_list("module__release_id", flat=True)
            .first()
        )

        if (
            enrollment_release_id is not None
            and lesson_release_id is not None
            and enrollment_release_id != lesson_release_id
        ):
            raise ValidationError(
                {
                    "lesson": (
                        "Lesson must belong to the enrollment's "
                        "course release."
                    ),
                }
            )

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

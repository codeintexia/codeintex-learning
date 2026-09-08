import uuid

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet

from .blocks import LessonSectionBlock


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
        FieldPanel("summary"),
        FieldPanel("level"),
        FieldPanel("audience"),
        FieldPanel("outcomes"),
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


@register_snippet
class CourseRelease(models.Model):
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


@register_snippet
class Module(models.Model):
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


@register_snippet
class Lesson(models.Model):
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

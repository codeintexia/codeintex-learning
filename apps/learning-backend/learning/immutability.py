from django.core.exceptions import ValidationError
from django.db import models


class PublishedReleaseMutationError(ValidationError):
    def __init__(self):
        super().__init__(
            (
                "Published course releases are immutable. "
                "Create a new CourseRelease instead."
            ),
            code="published_release_immutable",
        )


class CourseReleaseQuerySet(models.QuerySet):
    def _assert_mutable(self):
        if self.filter(is_published=True).exists():
            raise PublishedReleaseMutationError()

    def update(self, **kwargs):
        self._assert_mutable()
        return super().update(**kwargs)

    def delete(self):
        self._assert_mutable()
        return super().delete()


class ModuleQuerySet(models.QuerySet):
    def _assert_mutable(self):
        if self.filter(release__is_published=True).exists():
            raise PublishedReleaseMutationError()

    def update(self, **kwargs):
        self._assert_mutable()
        return super().update(**kwargs)

    def delete(self):
        self._assert_mutable()
        return super().delete()


class LessonQuerySet(models.QuerySet):
    def _assert_mutable(self):
        if self.filter(
            module__release__is_published=True
        ).exists():
            raise PublishedReleaseMutationError()

    def update(self, **kwargs):
        self._assert_mutable()
        return super().update(**kwargs)

    def delete(self):
        self._assert_mutable()
        return super().delete()

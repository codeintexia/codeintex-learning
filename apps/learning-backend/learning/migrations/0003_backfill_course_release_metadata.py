from django.db import migrations


def backfill_course_release_metadata(apps, schema_editor):
    CourseRelease = apps.get_model("learning", "CourseRelease")

    for release in CourseRelease.objects.select_related("course").iterator():
        course = release.course

        release.summary = course.summary
        release.level = course.level
        release.audience = course.audience
        release.outcomes = course.outcomes

        release.save(
            update_fields=[
                "summary",
                "level",
                "audience",
                "outcomes",
            ]
        )


def reverse_backfill_course_release_metadata(apps, schema_editor):
    CourseRelease = apps.get_model("learning", "CourseRelease")

    CourseRelease.objects.all().update(
        summary="",
        level="Foundation",
        audience="",
        outcomes="",
    )


class Migration(migrations.Migration):

    dependencies = [
        (
            "learning",
            "0002_courserelease_audience_courserelease_level_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(
            backfill_course_release_metadata,
            reverse_backfill_course_release_metadata,
        ),
    ]

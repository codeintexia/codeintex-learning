from wagtail import blocks


class LessonSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        required=False,
        max_length=255,
    )
    body = blocks.TextBlock()
    code = blocks.TextBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Lesson section"

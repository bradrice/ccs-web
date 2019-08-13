"""Streams live here"""

from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text and nothing else"""

    title = blocks.CharBlock(required=True, help_text="Add a title")
    text = blocks.TextBlock(required=True, help_text="Add your text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    subtitle = models.CharField(max_length=100, blank=False, null=True)
    left_col = RichTextField()
    right_col = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("left_col"),
        FieldPanel("right_col")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
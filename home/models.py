from django.db import models

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    PageChooserPanel, 
    MultiFieldPanel,
    InlinePanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1
    subpage_types = ['flex.FlexPage']

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

    # @route(r'^resource/(?P<cat_slug>[-\w]+)/?$')
    # def resources_page(self, request, cat_slug, *args, **kwargs):
    #     context = self.get_context(request, *args, **kwargs)
    #     context['a_special_test'] = cat_slug
    #     resources = Resource.objects.all()
    #     cats = ResourceCategory.objects.all()
    #     r = resources.get(resource_name="A New Day")
    #     rc = r.category
    #     print(cats)
    #     print(resources)
    #     print(rc)
    #     context['resources'] = resources
        
        
    #     return render(request, "home/resources_page.html", context)
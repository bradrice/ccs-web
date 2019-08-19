from django.db import models
from django.shortcuts import render
from wagtail.snippets.models import register_snippet
import uuid

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
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

class ResourceListingPage(RoutablePageMixin, Page):
    """Listing page lists all the Resource Pages."""

    template = "resourceservice/resource_listing_page.html"
    subpage_types = ['ResourcePage']
    max_count = 2

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def __str__(self):
        """String representation of this class"""
        return self.custom_title

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["resitems"] = ResourcePage.objects.live().public()
        return context

    @route(r'^resourcebycategory/(?P<cat_slug>[-\w]*)/$', name="category_view")
    def list_category_page(self, request, cat_slug, *args, **kwargs):
        print(cat_slug)
        context = self.get_context(request)
        try:
            category = ResourceCategory.objects.get(category_name=cat_slug)
        except Exception:
            category = None;

        if category is None:
            pass

        cats = ResourceCategory.objects.all()
        print(cats)
        print(category)
        ri = CategorySelectingOrderable.objects.filter(category__in=[category])
        print(ri)
        context['category'] = cat_slug
        context['resitems'] = CategorySelectingOrderable.objects.filter(category__in=[category])
        return render(request, "resourceservice/list_category_page.html", context)


# Create your models here.
class ResourcePage(Page):
    """Page for displaying resources"""    

    template = "resourceservice/resources_page.html"
    subpage_types = []

    subtitle = models.CharField(max_length=100, blank=False, null=True)
    resource_name = models.CharField(max_length=128, blank=False, null=True)
    phone_number = models.CharField(max_length=24, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    info = RichTextField(blank=True, null=True)
    # resource_category = models.ForeignKey("resourceservices.ResourceCategory", on_delete=models.CASCADE)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("subtitle")
            ], heading="Subtitle"
        ),
        MultiFieldPanel(
            [
                FieldPanel("resource_name"),
                FieldPanel("phone_number"),
            ],
            heading="Resource information"
        ),
        MultiFieldPanel(
            [
                FieldPanel('website')
            ],
            heading="Links"
        ),
        MultiFieldPanel(
            [
                FieldPanel('info')
            ],
            heading="Info"
        ),
        MultiFieldPanel(
            [
                InlinePanel("resource_category", label="Categories")
            ]
        )
    ]

    def __str__(self):
        return self.resource_name


class CategorySelectingOrderable(Orderable):
    """Category selecting orderable."""

    page = ParentalKey("resourceservice.ResourcePage", related_name="resource_category")
    category = models.ForeignKey("resourceservice.ResourceCategory", on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel("category")
    ]

    class Meta:
        verbose_name = "ResourceCategory"
        verbose_name_plural = "ResourceCategories"

    def __str__(self):
        return self.category.category_name


class ResourceCategory(models.Model):
    """Snippet for Resources category"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=128, blank=False, null=True)
    # page = ParentalKey("resourceservice.CategorySelectingOrderable", related_name="resource_category")


    panels = [
        MultiFieldPanel(
            [
                FieldPanel('category_name')
            ],
            heading="Category"
        )
    ]

    def __str__(self):
        """String representation of this class"""
        return self.category_name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

register_snippet(ResourceCategory)





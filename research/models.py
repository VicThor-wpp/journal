from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail import blocks
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index

from wagtailcodeblock.blocks import CodeBlock
from wagtail.snippets.models import register_snippet

class ResearchTagIndexPage(Page):
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        researchpages = ResearchPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['researchpages'] = researchpages
        return context

class ResearchIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        researchpages = self.get_children().live().order_by('-first_published_at')
        context['researchpages'] = researchpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class ResearchPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ResearchPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class ResearchPage(Page):
    date = models.DateField("Post date")
    abstract = models.TextField()
    paper_url = models.URLField(blank=True)
    code_url = models.URLField(blank=True)
    project_url = models.URLField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.TextBlock()),
        ('image', ImageChooserBlock()),
        ("code", CodeBlock(label='Code')),
        ('list', blocks.ListBlock(blocks.CharBlock(label="Fact"))),
    ], use_json_field=True)
    tags = ClusterTaggableManager(through=ResearchPageTag, blank=True)
    categories = ParentalManyToManyField('research.ResearchCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
        
    search_fields = Page.search_fields + [
        index.SearchField('abstract'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Research information"),
        FieldRowPanel([
            FieldPanel('project_url'),
            FieldPanel('paper_url'),
            FieldPanel('code_url'),
        ], heading="URL's information"),
        FieldPanel('abstract'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class ResearchPageGalleryImage(Orderable):
    page = ParentalKey(ResearchPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

@register_snippet
class ResearchCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'research categories'
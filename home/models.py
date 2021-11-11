from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock, RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.models import Page

from home.blocks import NewsBlock, ProductsBlock, SlideshowBlock, ArticleBlock, ArticleBlockTwo, ArticleProductBlock, \
    PhotoGalleryBlock


class HomePage(Page):
    body = StreamField(
        [
            ('title', CharBlock(label='Название страницы', help_text='Введите название страницы')),
            ('heading', RichTextBlock(features=['h1', 'h2', 'h3', 'hr', 'bold', 'italic'],
                                      label='Заголовок №1',
                                      help_text='Введите название заголовка')),
            ('caption', RichTextBlock(features=['h4', 'h5', 'h6', 'hr', 'bold', 'italic'],
                                      label='Заголовок №2',
                                      help_text='Введите название заголовка')),
            ('events_news', NewsBlock()),
            ('products', ProductsBlock()),
            ('slideshow', blocks.ListBlock(SlideshowBlock())),
            ('article', ArticleBlock()),
            ('article_two', ArticleBlockTwo()),
            ('article_product', ArticleProductBlock()),
            ('article_text', RichTextBlock(
                features=['bold', 'italic', 'enter'],
                label='Текстовый блок',
                help_text='Введите текст статьи',
                icon='form',
            )),
            ('photo_gallery', blocks.ListBlock(PhotoGalleryBlock())),

        ],
        # block_counts={
        #     'events_news': {'max_num': 1},
        #     'products': {'max_num': 1},
        # },
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

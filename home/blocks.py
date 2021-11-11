from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from django import forms


class NewsBlock(StructBlock):
    """Класс для формирования блока Мероприятия и новости"""
    class Meta:
        icon = 'snippet'
        template = 'tags/event_news.html'
        label = 'Фрагмент "Мероприятия и новости"'


class ProductsBlock(StructBlock):
    """Класс для формирования блока Карточки продукции и услуг"""
    class Meta:
        icon = 'snippet'
        template = 'tags/product_cards.html'
        label = 'Фрагмент "Карточки продукции и услуг"'


class SlideshowBlock(StructBlock):
    """Класс для формирования слайда в слайд-шоу"""

    figure = ImageChooserBlock(label='Картинка')
    caption = RichTextBlock(label='Название картинки', blank=True)
    description = RichTextBlock(label='Описание картинки', blank=True)

    class Meta:
        icon = 'view'
        label = 'Слайд'


class ArticleBlock(StructBlock):
    """Класс для формирования блока Статья (картинка слева)"""

    figure_first = ImageChooserBlock(label='Картинка слева')
    description = RichTextBlock(label='Статья (текст справа)')

    class Meta:
        icon = 'form'
        label = 'Статья (картинка слева)'


class ArticleBlockTwo(StructBlock):
    """Класс для формирования блока Статья (картинка справа)"""

    figure_second = ImageChooserBlock(label='Картинка справа')
    description_second = RichTextBlock(label='Статья (текст слева)')

    class Meta:
        icon = 'form'
        label = 'Статья (картинка справа)'


class ArticleProductBlock(StructBlock):
    """Класс для формирования блока Статья о продукции (услуге)"""

    image_product = ImageChooserBlock(label='Картинка слева')
    description_product = RichTextBlock(label='Статья (текст справа)')

    class Meta:
        icon = 'form'
        label = 'Статья о продукции (услуге)'


class PhotoGalleryBlock(StructBlock):
    """Класс для формирования картинки в фотогалерее"""

    figure = ImageChooserBlock(label='Картинка')

    class Meta:
        icon = 'image'
        label = 'Изображение фотогалереи'


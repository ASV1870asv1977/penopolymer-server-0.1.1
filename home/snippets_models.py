from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import MultiFieldPanel, StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.blocks import RichTextBlock, StructBlock, CharBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock

from wagtail.snippets.models import register_snippet


class ProductCardBlock(StructBlock):
    """Класс для формирования карточки продукции"""

    img_card_product = ImageChooserBlock(
        label='Изображение продукции',
        help_text='Загрузите изображение',
    )
    name_card_product = RichTextBlock(
        features=['bold', 'italic'],
        label='Наименование продукции',
        help_text='Введите название продукции',
    )
    description_card_product = RichTextBlock(
        features=['bold', 'italic'],
        label='Описание продукции',
        help_text='Введите описание продукции',
    )

    class Meta:
        template = 'blocks/product_card_block.html'
        label = 'Карточка продукции'


@register_snippet
class ProductCard(models.Model):
    """Класс для формирования фрагмента с карточками продукции"""

    card_product = StreamField(
        [
            ('product_card_block', ProductCardBlock()),
        ],
        blank=True,
        verbose_name='Карточки продукции',
    )

    panels = [
        MultiFieldPanel(
            [
                StreamFieldPanel('card_product'),
            ],
            heading='Карточки продукции'),
    ]

    class Meta:
        verbose_name = 'Карточка продукции'
        verbose_name_plural = 'Карточки продукции'

    def __str__(self):
        return 'Карточки продукции'


class EventCard(StructBlock):
    """Класс для формирования карточки мероприятия"""

    event_data = CharBlock(max_length=2, label="Число месяца")
    event_month = CharBlock(max_length=8, label="Месяц")
    event_name = RichTextBlock(
        max_length=200,
        null=True,
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        label='Название мероприятия',
        help_text='Введите название мероприятия',
    )
    event_description = RichTextBlock(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        null=True,
        label='Описание мероприятия',
        help_text='Введите описание мероприятия',
    )

    class Meta:
        template = 'blocks/event_block.html'
        label = 'Мероприятие'


class NewsCard(StructBlock):
    """Класс для формирования карточки новости"""

    news_data = CharBlock(max_length=2, label="Число месяца")
    news_month = CharBlock(max_length=8, label="Месяц")
    news_name = RichTextBlock(
        max_length=200,
        null=True,
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        label='Название новости',
        help_text='Введите название новости',
    )
    news_description = RichTextBlock(
        features=['bold', 'italic', 'ol', 'ul', 'link', 'enter'],
        null=True,
        label='Описание новости',
        help_text='Введите описание новости',
    )

    class Meta:
        template = 'blocks/news_block.html'
        label = 'Новость'


@register_snippet
class EventNewsPages(models.Model):
    """Класс для формирования фрагмента с календарем мероприятий и новостями"""

    events = StreamField(
        [
            ('events_block', EventCard()),
        ],
        blank=True,
        verbose_name='Мероприятия',
    )

    news = StreamField(
        [
            ('news_block', NewsCard()),
        ],
        blank=True,
        verbose_name='Новости',
    )

    panels = [
        MultiFieldPanel(
            [
                StreamFieldPanel('events'),
            ],
            heading='Мероприятия'),
        MultiFieldPanel(
            [
                StreamFieldPanel('news'),
            ],
            heading='Новости'),
    ]

    class Meta:
        verbose_name = 'Мероприятия и новости'
        verbose_name_plural = 'Мероприятия и новости'

    def __str__(self):
        return 'Мероприятия и новости'


@register_snippet
class Header(models.Model):
    """Класс для формирования фрагмента хедера сайта"""

    telephones = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    panels = [
        FieldPanel('telephones'),
        FieldPanel('address'),
    ]

    class Meta:
        verbose_name = 'Хедер'
        verbose_name_plural = 'Хедеры'

    def __str__(self):
        return self.text


@register_snippet
class Footer(models.Model):
    """Класс для формирования фрагмента футера сайта"""

    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    telephones = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    email = models.EmailField(
        verbose_name="Email предприятия",
    )

    panels = [
        FieldPanel('address'),
        FieldPanel('telephones'),
        FieldPanel('email'),
    ]

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return 'Футер'

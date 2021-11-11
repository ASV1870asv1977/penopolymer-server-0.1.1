# Generated by Django 3.2.9 on 2021-11-10 15:11

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock(help_text='Введите название страницы', label='Название страницы')), ('heading', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h6', 'hr', 'bold', 'italic'], help_text='Введите название заголовка', label='Заголовок №1')), ('caption', wagtail.core.blocks.RichTextBlock(features=['h4', 'h5', 'h6', 'hr', 'bold', 'italic'], help_text='Введите название заголовка', label='Заголовок №2')), ('events_news', wagtail.core.blocks.StructBlock([])), ('products', wagtail.core.blocks.StructBlock([])), ('slideshow', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('figure', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('caption', wagtail.core.blocks.RichTextBlock(label='Название картинки')), ('description', wagtail.core.blocks.RichTextBlock(label='Описание картинки'))])))], blank=True),
        ),
    ]
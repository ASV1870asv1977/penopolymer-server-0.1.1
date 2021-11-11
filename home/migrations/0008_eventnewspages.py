# Generated by Django 3.2.9 on 2021-11-10 07:54

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20211110_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventNewsPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events_news', wagtail.core.fields.StreamField([('events_block', wagtail.core.blocks.StructBlock([])), ('news_block', wagtail.core.blocks.StructBlock([]))], blank=True, verbose_name='Карточки продукции')),
            ],
            options={
                'verbose_name': 'Мероприятия и новости',
                'verbose_name_plural': 'Мероприятия и новости',
            },
        ),
    ]
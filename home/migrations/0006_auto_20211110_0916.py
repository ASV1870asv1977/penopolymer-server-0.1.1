# Generated by Django 3.2.9 on 2021-11-10 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('home', '0005_alter_productcard_card_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcard',
            name='id',
        ),
        migrations.AddField(
            model_name='productcard',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, default=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page'),
            preserve_default=False,
        ),
    ]

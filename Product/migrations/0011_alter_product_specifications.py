# Generated by Django 4.1.3 on 2023-01-11 16:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
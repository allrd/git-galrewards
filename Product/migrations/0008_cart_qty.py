# Generated by Django 4.1.3 on 2022-12-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
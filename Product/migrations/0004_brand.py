# Generated by Django 4.1.3 on 2022-11-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-24 19:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=50)),
                ('purchaseCurrency', models.CharField(choices=[('ghs', 'GHS'), ('usd', 'USD')], default='ghs', max_length=3)),
                ('purchaseAmount', models.CharField(max_length=25)),
                ('usdConversionRate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costInUsd', models.IntegerField()),
                ('perPointCost', models.DecimalField(decimal_places=4, default=0.018, max_digits=5)),
                ('points', models.IntegerField()),
                ('specifications', tinymce.models.HTMLField()),
                ('status', models.BooleanField(default=True)),
                ('productImage', models.ImageField(default=None, max_length=250, null=True, upload_to='product/')),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.brand', to_field='Brand')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.category', to_field='category')),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.subcategory', to_field='subCategory')),
            ],
        ),
    ]

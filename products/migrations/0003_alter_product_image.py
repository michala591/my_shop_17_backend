# Generated by Django 5.1.4 on 2024-12-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, default='https://example.com/placeholder.png', max_length=500, null=True),
        ),
    ]

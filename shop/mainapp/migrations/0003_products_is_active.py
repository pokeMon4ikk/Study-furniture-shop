# Generated by Django 4.0 on 2021-12-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_productsitem_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
# Generated by Django 4.0 on 2022-01-21 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_rename_aboutme_shopuserprofile_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='authapp.shopuser'),
        ),
    ]
# Generated by Django 2.2.28 on 2024-02-09 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20240209_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='pictur',
            new_name='picture',
        ),
    ]

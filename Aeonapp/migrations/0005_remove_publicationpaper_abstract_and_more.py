# Generated by Django 5.0.6 on 2024-06-20 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aeonapp', '0004_publicationpaper'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationpaper',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='publicationpaper',
            name='journal',
        ),
    ]

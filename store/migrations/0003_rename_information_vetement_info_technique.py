# Generated by Django 5.0.6 on 2024-06-23 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_vetement_image_vetement_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vetement',
            old_name='information',
            new_name='info_technique',
        ),
    ]

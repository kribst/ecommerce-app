# Generated by Django 5.0.6 on 2024-06-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vetement',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vetement',
            name='information',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
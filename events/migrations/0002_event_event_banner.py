# Generated by Django 4.2.13 on 2024-07-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_banner',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]

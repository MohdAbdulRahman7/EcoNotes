# Generated by Django 4.2.13 on 2024-07-19 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_alter_member_options_alter_member_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.AlterModelManagers(
            name='member',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

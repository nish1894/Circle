# Generated by Django 5.2.1 on 2025-06-06 05:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0005_alter_groupmessage_body'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='users_online',
            field=models.ManyToManyField(blank=True, related_name='online_users', to=settings.AUTH_USER_MODEL),
        ),
    ]

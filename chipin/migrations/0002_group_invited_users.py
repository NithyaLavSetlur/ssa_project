# Generated by Django 5.1.2 on 2024-11-21 15:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='invited_users',
            field=models.ManyToManyField(blank=True, related_name='pending_invitations', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 5.0.1 on 2024-05-19 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_profile_identity_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='user_title',
        ),
    ]

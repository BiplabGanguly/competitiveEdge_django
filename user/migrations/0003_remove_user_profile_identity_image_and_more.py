# Generated by Django 5.0.1 on 2024-05-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_address_user_data_user_profile_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='identity_image',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='identity_number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

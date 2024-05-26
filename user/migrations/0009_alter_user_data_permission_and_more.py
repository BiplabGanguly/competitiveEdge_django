# Generated by Django 5.0.6 on 2024-05-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_userbranch_user_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='permission',
            field=models.CharField(choices=[('pending', 'pending'), ('accept', 'accept'), ('reject', 'reject')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='userbranch',
            name='user_permission',
            field=models.CharField(choices=[('pending', 'pending'), ('accept', 'accept'), ('reject', 'reject')], default='pending', max_length=50),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-15 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_authorization_field_authorized_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteaccount',
            name='validation_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

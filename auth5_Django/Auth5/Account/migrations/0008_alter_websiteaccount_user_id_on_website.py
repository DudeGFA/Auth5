# Generated by Django 4.2.7 on 2023-12-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_websiteaccount_validation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteaccount',
            name='user_id_on_website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
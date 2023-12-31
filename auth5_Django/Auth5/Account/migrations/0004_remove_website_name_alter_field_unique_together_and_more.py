# Generated by Django 4.2.7 on 2023-12-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_alter_userprofile_user_alter_website_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='name',
        ),
        migrations.AlterUniqueTogether(
            name='field',
            unique_together={('group', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='fieldgroup',
            unique_together={('owner', 'name')},
        ),
    ]

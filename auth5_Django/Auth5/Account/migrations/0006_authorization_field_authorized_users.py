# Generated by Django 4.2.7 on 2023-12-13 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_website_callback_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.field')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.userprofile')),
            ],
            options={
                'unique_together': {('field', 'user_profile')},
            },
        ),
        migrations.AddField(
            model_name='field',
            name='authorized_users',
            field=models.ManyToManyField(related_name='authorized_fields', through='Account.Authorization', to='Account.userprofile'),
        ),
    ]

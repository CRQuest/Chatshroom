# Generated by Django 2.0.4 on 2018-05-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]

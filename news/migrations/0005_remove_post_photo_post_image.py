# Generated by Django 4.2.2 on 2023-06-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='images/'),
        ),
    ]

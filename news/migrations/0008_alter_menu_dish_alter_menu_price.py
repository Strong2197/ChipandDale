# Generated by Django 4.2.2 on 2023-06-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_menu_alter_post_options_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish',
            field=models.CharField(max_length=100, verbose_name='Страва'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Ціна'),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-02 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_multipleimage_postid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleImageKids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(max_length=200, null=True, upload_to='', verbose_name='Фото')),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.attracs')),
            ],
            options={
                'verbose_name': 'Фото до Атракціонів',
                'verbose_name_plural': 'Фото до Атракціонів',
            },
        ),
    ]

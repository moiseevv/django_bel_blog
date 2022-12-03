# Generated by Django 3.2.3 on 2022-12-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]

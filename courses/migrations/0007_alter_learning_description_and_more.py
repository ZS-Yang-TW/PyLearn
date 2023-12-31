# Generated by Django 4.2.1 on 2023-12-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_video_is_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='description',
            field=models.CharField(default='Course Property Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='description',
            field=models.CharField(default='Course Property Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(default='Course Property Description', max_length=100),
        ),
    ]

# Generated by Django 4.2.1 on 2023-12-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Course Name', max_length=30)),
                ('description', models.CharField(default='Course Description', max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnail')),
                ('date', models.DateField(auto_now_add=True)),
                ('resource', models.FileField(upload_to='files/resource')),
                ('length', models.IntegerField(default=0)),
            ],
        ),
    ]

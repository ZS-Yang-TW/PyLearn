# Generated by Django 5.0 on 2023-12-27 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0016_payment_course_payment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="user_course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.usercourse",
            ),
        ),
    ]
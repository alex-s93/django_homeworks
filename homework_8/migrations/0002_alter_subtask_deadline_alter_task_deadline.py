# Generated by Django 5.0.6 on 2024-05-29 15:23

import homework_8.models.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_8', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='deadline',
            field=models.DateTimeField(validators=[homework_8.models.validators.validate_future_date]),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(validators=[homework_8.models.validators.validate_future_date]),
        ),
    ]
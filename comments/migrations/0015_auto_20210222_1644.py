# Generated by Django 2.2.18 on 2021-02-22 08:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0014_auto_20210207_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 22, 8, 44, 51, 130269, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
# Generated by Django 2.2.18 on 2021-02-06 03:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20210205_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 3, 2, 47, 74075, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]

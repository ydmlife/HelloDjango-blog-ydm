# Generated by Django 2.2.18 on 2021-02-05 09:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20210205_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 9, 14, 15, 202883, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]

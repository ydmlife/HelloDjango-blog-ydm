# Generated by Django 2.2.18 on 2021-02-23 06:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0017_merge_20210223_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 6, 29, 43, 385819, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]

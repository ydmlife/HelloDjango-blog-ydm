# Generated by Django 2.2.18 on 2021-02-05 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20210205_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 9, 11, 7, 172466, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
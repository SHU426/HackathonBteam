# Generated by Django 4.0.2 on 2022-03-11 21:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0004_sred_msg_post_msg_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sred_msg_post',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 21, 55, 29, 131791, tzinfo=utc), verbose_name='メッセージ送信日時'),
        ),
        migrations.AlterField(
            model_name='sredmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 21, 55, 29, 128716, tzinfo=utc), verbose_name='掲示板作成日時'),
        ),
    ]
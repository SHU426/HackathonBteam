# Generated by Django 4.0.2 on 2022-03-11 21:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_sredmodel_created_at_sredmodel_delete_flg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sred_msg_post',
            name='msg_author',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sred_msg_post',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 21, 53, 29, 520518, tzinfo=utc), verbose_name='メッセージ送信日時'),
        ),
        migrations.AlterField(
            model_name='sredmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 21, 53, 29, 519127, tzinfo=utc), verbose_name='掲示板作成日時'),
        ),
    ]
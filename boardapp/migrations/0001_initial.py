# Generated by Django 4.0.2 on 2022-02-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255, verbose_name='名前')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('delete_flg', models.SmallIntegerField(default=0, verbose_name='削除フラグ')),
            ],
        ),
    ]

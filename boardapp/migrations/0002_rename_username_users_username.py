# Generated by Django 4.0.2 on 2022-02-23 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='Username',
            new_name='username',
        ),
    ]
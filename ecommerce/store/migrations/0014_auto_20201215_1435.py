# Generated by Django 3.1.3 on 2020-12-15 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20201215_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='deleted_at',
        ),
    ]

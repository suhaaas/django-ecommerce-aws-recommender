# Generated by Django 3.1.3 on 2021-01-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='new user', max_length=30),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
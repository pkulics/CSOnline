# Generated by Django 2.0.2 on 2019-09-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190921_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], default='female', max_length=10, verbose_name='性别'),
        ),
    ]

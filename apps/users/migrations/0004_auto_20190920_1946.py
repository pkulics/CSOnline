# Generated by Django 2.0.2 on 2019-09-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190920_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('forget', '找回密码'), ('register', '注册')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], default='female', max_length=10, verbose_name='性别'),
        ),
    ]

# Generated by Django 2.0.2 on 2019-09-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190922_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('forget', '找回密码'), ('register', '注册')], max_length=10),
        ),
    ]
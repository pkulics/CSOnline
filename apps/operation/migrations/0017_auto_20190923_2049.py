# Generated by Django 2.0.2 on 2019-09-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0016_auto_20190923_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(3, '讲师'), (2, '课程机构'), (1, '课程')], default=1, verbose_name='收藏类型'),
        ),
    ]
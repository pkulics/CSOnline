# Generated by Django 2.0.2 on 2019-09-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0012_auto_20190923_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(2, '课程机构'), (3, '讲师'), (1, '课程')], default=1, verbose_name='收藏类型'),
        ),
    ]

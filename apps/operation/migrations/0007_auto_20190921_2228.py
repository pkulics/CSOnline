# Generated by Django 2.0.2 on 2019-09-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_auto_20190920_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(2, '课程机构'), (1, '课程'), (3, '讲师')], default=1, verbose_name='收藏类型'),
        ),
    ]
# Generated by Django 2.0.2 on 2019-09-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_auto_20190923_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('gj', '高级'), ('zj', '中级')], max_length=2, verbose_name='难度'),
        ),
    ]

# Generated by Django 2.0.2 on 2019-09-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20190920_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('gj', '高级'), ('zj', '中级')], max_length=2, verbose_name='难度'),
        ),
    ]
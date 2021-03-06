# Generated by Django 2.2.4 on 2020-11-18 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0002_auto_20201118_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='succeededuser',
            options={'ordering': ('-timeend',), 'verbose_name': '最新成交', 'verbose_name_plural': '最新成交'},
        ),
        migrations.RemoveField(
            model_name='succeededuser',
            name='timeat',
        ),
        migrations.AddField(
            model_name='succeededuser',
            name='timeend',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='结束时间'),
        ),
        migrations.AddField(
            model_name='succeededuser',
            name='timestart',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='开始时间'),
        ),
    ]

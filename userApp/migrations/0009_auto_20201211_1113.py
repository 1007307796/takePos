# Generated by Django 2.2.4 on 2020-12-11 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0008_auto_20201204_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '待支付'), (2, '支付未成功'), (3, '运行中'), (4, '已取消'), (5, '已成功占座'), (6, '占座失败')], default=1, verbose_name='订单状态'),
        ),
    ]
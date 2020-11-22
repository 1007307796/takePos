# Generated by Django 2.2.4 on 2020-11-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productType',
            field=models.CharField(choices=[('education', '学历类考试'), ('technology', '计算机类考试'), ('economic', '金融类考试'), ('language', '语言类考试')], max_length=50, verbose_name='服务类型'),
        ),
    ]

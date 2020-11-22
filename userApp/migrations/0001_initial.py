# Generated by Django 2.2.4 on 2020-11-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, verbose_name='用户名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('headsculpture', models.ImageField(blank=True, upload_to='headsculpture/', verbose_name='头像')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
# Generated by Django 2.2.4 on 2020-11-18 06:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('email', models.EmailField(max_length=30, verbose_name='邮箱')),
                ('title', models.CharField(max_length=30, verbose_name='问题标题')),
                ('fdtype', models.CharField(default='吐槽交流', max_length=8, verbose_name='问题类型')),
                ('question', models.TextField(blank=True, null=True, verbose_name='问题详情')),
                ('image', models.ImageField(blank=True, null=True, upload_to='contact/feedback/%Y_%m_%d', verbose_name='问题截图')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='回复')),
                ('publishtime', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='提交时间')),
                ('replytime', models.DateTimeField(auto_now=True, max_length=20, null=True, verbose_name='回复时间')),
                ('status', models.IntegerField(choices=[(1, '待审核'), (2, '待回复'), (3, '未通过'), (4, '已完成')], default=1, verbose_name='问题状态')),
            ],
            options={
                'verbose_name': '工单',
                'verbose_name_plural': '工单',
                'ordering': ('-status', '-publishtime'),
            },
        ),
        migrations.CreateModel(
            name='SchoolToPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='考点名称')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='纬度')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='经度')),
            ],
            options={
                'verbose_name': '考点经纬度',
                'verbose_name_plural': '考点经纬度',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='资料名称')),
                ('files', models.FileField(blank=True, upload_to='contact/software/', verbose_name='文件')),
                ('uploadtime', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='上传时间')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='下载量')),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件',
                'ordering': ['-uploadtime'],
            },
        ),
    ]

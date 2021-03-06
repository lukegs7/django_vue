# Generated by Django 2.2.10 on 2020-05-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='环境名称')),
                ('url', models.CharField(max_length=50, verbose_name='访问地址')),
                ('status', models.IntegerField(choices=[(0, '离线'), (1, '在线')], default=0, verbose_name='在线状态')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=200, verbose_name='备注')),
            ],
            options={
                'db_table': 'environment',
            },
        ),
    ]

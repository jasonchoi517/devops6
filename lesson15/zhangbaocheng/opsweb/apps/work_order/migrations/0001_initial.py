# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='echarts_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=10, verbose_name='\u63d0\u4ea4\u4eba')),
                ('web', models.CharField(max_length=10, verbose_name='Web\u7c7b\u578b')),
                ('db', models.CharField(max_length=10, verbose_name='DB\u7c7b\u578b')),
                ('crontab', models.CharField(max_length=10, verbose_name='crontab\u7c7b\u578b')),
                ('conf', models.CharField(max_length=10, verbose_name='conf\u7c7b\u578b')),
                ('other', models.CharField(max_length=10, verbose_name='other\u7c7b\u578b')),
                ('data_collection_time', models.CharField(max_length=10, verbose_name='\u6570\u636e\u6536\u96c6\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u5de5\u5355\u6807\u9898')),
                ('type', models.IntegerField(choices=[(0, '\u6570\u636e\u5e93'), (1, 'WEB\u670d\u52a1'), (2, '\u8ba1\u5212\u4efb\u52a1'), (3, '\u914d\u7f6e\u6587\u4ef6'), (4, '\u5176\u5b83')], default=0, verbose_name='\u5de5\u5355\u7c7b\u578b')),
                ('order_contents', models.TextField(verbose_name='\u5de5\u5355\u5185\u5bb9')),
                ('status', models.IntegerField(choices=[(0, '\u7533\u8bf7'), (1, '\u5904\u7406\u4e2d'), (2, '\u5b8c\u6210'), (3, '\u5931\u8d25')], default=0, verbose_name='\u5de5\u5355\u72b6\u6001')),
                ('result_desc', models.TextField(blank=True, null=True, verbose_name='\u5904\u7406\u7ed3\u679c')),
                ('apply_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('complete_time', models.DateTimeField(auto_now=True, verbose_name='\u5904\u7406\u5b8c\u6210\u65f6\u95f4')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_order_applicant', to=settings.AUTH_USER_MODEL, verbose_name='\u7533\u8bf7\u4eba')),
                ('assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6307\u6d3e\u7ed9')),
            ],
            options={
                'ordering': ['-complete_time'],
                'verbose_name': 'work_order',
                'verbose_name_plural': 'work_order',
            },
        ),
    ]

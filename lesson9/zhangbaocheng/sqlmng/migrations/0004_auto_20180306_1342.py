# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlmng', '0003_auto_20180306_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbconf',
            name='name',
            field=models.CharField(max_length=32, verbose_name='\u540d\u5b57'),
        ),
        migrations.AlterField(
            model_name='inceptsql',
            name='name',
            field=models.CharField(max_length=32, verbose_name='\u540d\u5b57'),
        ),
    ]
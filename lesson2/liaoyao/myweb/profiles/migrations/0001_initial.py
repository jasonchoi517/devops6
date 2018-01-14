# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 08:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(blank=True, default='', max_length=11, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('address', models.CharField(blank=True, default='', max_length=128, verbose_name='\u5730\u5740')),
            ],
        ),
    ]
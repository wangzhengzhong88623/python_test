# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-23 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user_type_id',
        ),
    ]

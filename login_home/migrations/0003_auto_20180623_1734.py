# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-23 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_home', '0002_remove_userinfo_user_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_home.UserGroup'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-26 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32, unique=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=32, verbose_name='用户名')),
                ('password', models.CharField(help_text='pwd', max_length=60)),
                ('email', models.CharField(max_length=60, null=True)),
                ('test', models.EmailField(error_messages={'invalid': '请输入密码'}, max_length=19, null=True)),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_home.UserGroup')),
            ],
        ),
    ]

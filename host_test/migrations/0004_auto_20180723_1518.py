# Generated by Django 2.0.6 on 2018-07-23 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_test', '0003_application_hosttoapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosttoapp',
            name='aobj',
        ),
        migrations.RemoveField(
            model_name='hosttoapp',
            name='hobj',
        ),
        migrations.DeleteModel(
            name='HostToApp',
        ),
    ]

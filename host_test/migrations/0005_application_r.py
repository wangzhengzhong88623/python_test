# Generated by Django 2.0.6 on 2018-07-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_test', '0004_auto_20180723_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='r',
            field=models.ManyToManyField(to='host_test.Host_test'),
        ),
    ]

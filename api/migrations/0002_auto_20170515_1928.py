# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucketlist',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='bucketlist',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='bucketlist',
            name='name',
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='anonymity',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='connection_type',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='country',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='ip',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bucketlist',
            name='port',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='id',
            field=models.CharField(default='SOME STRING', max_length=140, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='bucketlist',
            table='Bucketlist',
        ),
    ]
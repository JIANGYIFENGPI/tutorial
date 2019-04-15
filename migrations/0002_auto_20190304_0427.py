# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-04 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=45)),
                ('Director', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]

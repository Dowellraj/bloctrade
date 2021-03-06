# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-21 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloctradeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=2000, null=True)),
                ('emailId', models.EmailField(max_length=2000)),
                ('password', models.CharField(max_length=2000, null=True)),
                ('contactNumber', models.CharField(max_length=2000, null=True)),
                ('role', models.CharField(max_length=2000, null=True)),
                ('userStatus', models.CharField(default='Active', max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userToken',
            fields=[
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=2000, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]

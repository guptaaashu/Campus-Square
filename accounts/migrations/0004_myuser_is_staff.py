# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-12 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_myuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
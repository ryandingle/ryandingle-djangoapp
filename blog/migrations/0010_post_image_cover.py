# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160430_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_cover',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]

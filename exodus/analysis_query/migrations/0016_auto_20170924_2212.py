# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0015_auto_20170924_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='apk',
            field=models.FileField(upload_to='apks/a4b4d4d6-0a3b-478d-9d67-099b699ec7fc'),
        ),
        migrations.AlterField(
            model_name='analysisrequest',
            name='storage_path',
            field=models.TextField(default='apks/a4b4d4d6-0a3b-478d-9d67-099b699ec7fc'),
        ),
    ]

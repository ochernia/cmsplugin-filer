# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 09:26
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_folder', '0003_auto_20160713_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerfolder',
            name='folder',
            field=filer.fields.folder.FilerFolderField(null=True, on_delete=django.db.models.deletion.PROTECT, to='filer.Folder'),
        ),
    ]

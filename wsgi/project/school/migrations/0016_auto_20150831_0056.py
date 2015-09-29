# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20150831_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletters',
            name='file',
            field=models.FileField(upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='policies',
            name='file',
            field=models.FileField(upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='schoolmenu',
            name='menu',
            field=models.FileField(upload_to='documents'),
        ),
    ]

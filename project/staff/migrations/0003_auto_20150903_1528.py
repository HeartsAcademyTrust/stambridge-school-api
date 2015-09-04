# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20150901_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]

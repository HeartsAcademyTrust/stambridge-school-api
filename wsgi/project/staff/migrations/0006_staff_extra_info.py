# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20150911_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='extra_info',
            field=models.TextField(blank=True),
        ),
    ]

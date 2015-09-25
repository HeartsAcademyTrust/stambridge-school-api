# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_auto_20150918_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolmenu',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]

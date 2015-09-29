# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20150828_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletters',
            name='month',
        ),
        migrations.RemoveField(
            model_name='newsletters',
            name='year',
        ),
        migrations.AddField(
            model_name='newsletters',
            name='date_published',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]

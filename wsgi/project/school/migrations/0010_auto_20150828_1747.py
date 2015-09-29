# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20150828_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletters',
            name='date_published',
            field=models.DateField(null=True),
        ),
    ]

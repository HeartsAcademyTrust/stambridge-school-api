# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20150828_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletters',
            name='school',
            field=models.OneToOneField(null=True, to='school.School'),
        ),
    ]

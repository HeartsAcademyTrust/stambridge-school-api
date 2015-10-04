# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0024_curriculum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='title',
        ),
    ]

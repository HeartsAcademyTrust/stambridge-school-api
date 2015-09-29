# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150911_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='holiday',
            new_name='term',
        ),
    ]

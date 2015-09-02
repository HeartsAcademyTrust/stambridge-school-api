# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_policies'),
    ]

    operations = [
        migrations.AddField(
            model_name='policies',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

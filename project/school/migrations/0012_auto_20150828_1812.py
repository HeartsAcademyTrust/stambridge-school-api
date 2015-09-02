# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_newsletters_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletters',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='newsletters',
            name='school',
            field=models.ForeignKey(to='school.School'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20150903_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(to='staff.Department', related_name='staff'),
        ),
        migrations.AlterUniqueTogether(
            name='staff',
            unique_together=set([('department', 'id')]),
        ),
    ]

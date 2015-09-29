# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_auto_20150911_2151'),
        ('staff', '0004_auto_20150911_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['role']},
        ),
        migrations.RemoveField(
            model_name='staff',
            name='school',
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(to='school.School'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='department',
            field=models.ForeignKey(to='staff.Department', related_name='vacancies'),
        ),
        migrations.AlterUniqueTogether(
            name='vacancy',
            unique_together=set([('department', 'id')]),
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='school',
        ),
    ]

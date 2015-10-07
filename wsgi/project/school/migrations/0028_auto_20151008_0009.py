# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0027_auto_20151004_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='title',
            field=models.CharField(default=b'Curriculum', max_length=50),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='school',
            field=models.ForeignKey(to='school.School'),
        ),
    ]

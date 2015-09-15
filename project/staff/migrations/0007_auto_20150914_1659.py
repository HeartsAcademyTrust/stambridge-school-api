# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_staff_extra_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(upload_to='images', width_field=279, height_field=329),
        ),
    ]

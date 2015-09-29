# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_auto_20150911_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuatoryinfo',
            name='file',
            field=models.FileField(upload_to='statuaryInfo', null=True),
        ),
    ]

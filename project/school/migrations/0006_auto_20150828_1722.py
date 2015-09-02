# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_schoolmenu_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolmenu',
            name='menu',
            field=models.FileField(upload_to='files'),
        ),
        migrations.AlterField(
            model_name='schoolmenu',
            name='school',
            field=models.OneToOneField(to='school.School'),
        ),
    ]

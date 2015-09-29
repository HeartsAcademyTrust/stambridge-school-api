# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20150828_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('menu', models.FileField(upload_to='')),
            ],
        ),
    ]

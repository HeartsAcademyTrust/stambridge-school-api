# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20150828_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='files')),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20150828_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('year', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(2000)])),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
    ]

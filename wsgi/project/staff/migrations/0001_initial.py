# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_auto_20150831_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images')),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('role', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
    ]

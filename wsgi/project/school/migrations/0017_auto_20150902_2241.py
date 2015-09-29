# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_auto_20150831_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='documents')),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='documents')),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
        migrations.RemoveField(
            model_name='newsletters',
            name='school',
        ),
        migrations.RemoveField(
            model_name='policies',
            name='school',
        ),
        migrations.DeleteModel(
            name='Newsletters',
        ),
        migrations.DeleteModel(
            name='Policies',
        ),
    ]

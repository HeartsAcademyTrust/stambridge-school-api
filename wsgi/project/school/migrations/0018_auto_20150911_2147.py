# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20150902_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=20)),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
        migrations.CreateModel(
            name='StatuaryInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='statuaryInfo')),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='file',
            field=models.FileField(upload_to='newsletters'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='file',
            field=models.FileField(upload_to='policies'),
        ),
    ]

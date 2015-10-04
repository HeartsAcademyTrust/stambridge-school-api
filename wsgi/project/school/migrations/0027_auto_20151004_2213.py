# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0026_admissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolHomework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('deadline', models.DateField()),
                ('file', models.FileField(upload_to=b'lettersHome')),
                ('year', models.ForeignKey(related_name='homework', to='school.SchoolYear')),
            ],
            options={
                'ordering': ['deadline'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='schoolhomework',
            unique_together=set([('year', 'title')]),
        ),
    ]

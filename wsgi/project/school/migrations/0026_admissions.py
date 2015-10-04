# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0025_remove_curriculum_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra_notes', models.TextField(blank=True)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to=b'admissions')),
                ('school', models.OneToOneField(to='school.School')),
            ],
        ),
    ]

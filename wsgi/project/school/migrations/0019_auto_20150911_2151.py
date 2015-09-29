# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0018_auto_20150911_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatuatoryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='statuaryInfo')),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
        migrations.RemoveField(
            model_name='statuaryinfo',
            name='school',
        ),
        migrations.DeleteModel(
            name='StatuaryInfo',
        ),
    ]

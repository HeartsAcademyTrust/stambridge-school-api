# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0020_auto_20150912_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolLetters',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('deadline', models.DateField()),
                ('file', models.FileField(upload_to='lettersHome')),
                ('year', models.ForeignKey(related_name='letters', to='school.SchoolYear')),
            ],
            options={
                'ordering': ['deadline'],
            },
        ),
        migrations.CreateModel(
            name='StatutoryInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('file', models.FileField(null=True, upload_to='statuaryInfo')),
                ('school', models.ForeignKey(to='school.School')),
            ],
        ),
        migrations.RemoveField(
            model_name='statuatoryinfo',
            name='school',
        ),
        migrations.DeleteModel(
            name='StatuatoryInfo',
        ),
        migrations.AlterUniqueTogether(
            name='schoolletters',
            unique_together=set([('year', 'title')]),
        ),
    ]

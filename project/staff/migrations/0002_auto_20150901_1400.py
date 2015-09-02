# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(to='staff.Department'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='department',
            field=models.ForeignKey(to='staff.Department'),
        ),
    ]

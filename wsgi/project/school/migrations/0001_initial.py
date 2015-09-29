# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2, default='BR', choices=[('BR', 'Brisoe Primary School'), ('WI', 'Wickford Church of England School'), ('WA', 'Waterman Primary School'), ('ST', 'Stambridge Primary School'), ('HE', 'Hearts Academy Trust')])),
            ],
        ),
    ]

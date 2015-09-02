# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def import_schools(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    School = apps.get_model("school", "School")
    db_alias = schema_editor.connection.alias
    School.objects.using(db_alias).bulk_create([
        School(name="Hearts Academy Trust"),
        School(name="Stambridge Primary School"),
        School(name="Waterman Primary School"),
        School(name="Wickford Church of England School"),
        School(name="Brisoe Primary School and Nursery"),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_policies_date_published'),
    ]

    operations = [
    	migrations.RunPython(import_schools),
    ]

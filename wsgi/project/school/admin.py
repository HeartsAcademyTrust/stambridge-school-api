from django.contrib import admin
from .models import School, SchoolYear, SchoolMenu, SchoolLetters, SchoolHomework, StatutoryInfo, Newsletter, Policy, Performance, Curriculum, Admissions

admin.site.register(School)
admin.site.register(SchoolYear)
admin.site.register(SchoolMenu)
admin.site.register(SchoolLetters)
admin.site.register(SchoolHomework)
admin.site.register(Newsletter)
admin.site.register(Policy)
admin.site.register(StatutoryInfo)
admin.site.register(Performance)
admin.site.register(Curriculum)
admin.site.register(Admissions)
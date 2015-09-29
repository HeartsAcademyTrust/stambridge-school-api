from django.contrib import admin
from .models import School, SchoolYear, SchoolMenu, SchoolLetters, StatutoryInfo, Newsletter, Policy

admin.site.register(School)
admin.site.register(SchoolYear)
admin.site.register(SchoolMenu)
admin.site.register(SchoolLetters)
admin.site.register(Newsletter)
admin.site.register(Policy)
admin.site.register(StatutoryInfo)
from django.contrib import admin
from .models import School, SchoolMenu, StatuatoryInfo, Newsletter, Policy

admin.site.register(School)
admin.site.register(SchoolMenu)
admin.site.register(Newsletter)
admin.site.register(Policy)
admin.site.register(StatuatoryInfo)
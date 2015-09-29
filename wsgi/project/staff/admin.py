from django.contrib import admin
from .models import Department, Staff, Vacancy

admin.site.register(Staff)
admin.site.register(Vacancy)
admin.site.register(Department)
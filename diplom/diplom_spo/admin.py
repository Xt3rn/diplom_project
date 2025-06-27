from django.contrib import admin
from .models import Diplom


@admin.register(Diplom)
class DiplomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student_name', 'org_name', 'title',
                    'year', 'description', )
    search_fields = ('student_name', 'org_name', 'year',)

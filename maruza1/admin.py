from django.contrib import admin
from maruza1.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'birth_year', 'category', 'subject')
    list_editable = ('name','birth_year', 'category', 'subject')
    search_fields = ('name', 'subject')
    list_filter = ('category', 'subject')


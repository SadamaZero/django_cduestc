from django.contrib import admin
from .models import StudentInfo


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('xuehao', 'user', 'teacher', 'thesis', 'type')

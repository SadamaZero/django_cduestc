from django.contrib import admin
from .models import TeacherInfo, Type, ThesisInfo


@admin.register(TeacherInfo)
class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_class')


@admin.register(ThesisInfo)
class ThesisInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'title', 'type')

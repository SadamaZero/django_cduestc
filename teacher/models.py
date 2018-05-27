from django.db import models
from django.contrib.auth.models import User


class TeacherInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return '%s老师' % self.user.username


class Type(models.Model):
    type_class = models.CharField(max_length=20)

    def __str__(self):
        return self.type_class


class ThesisInfo(models.Model):
    title = models.CharField(max_length=50, null=False)
    teacher = models.ForeignKey(TeacherInfo, on_delete=models.CASCADE)
    limit_time = models.DateField(auto_now=False, auto_now_add=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title

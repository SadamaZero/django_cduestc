from django.db import models
from django.contrib.auth.models import User
from teacher.models import TeacherInfo, ThesisInfo, Type


class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xuehao = models.IntegerField(max_length=10, unique=True, null=False)
    teacher = models.ForeignKey(TeacherInfo, on_delete=models.DO_NOTHING)
    thesis = models.ForeignKey(ThesisInfo, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)

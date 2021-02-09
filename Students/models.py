from django.db import models
from Teacher.models import Teacher


class Sudent(models.Model):
    name = models.CharField("ФИО", max_length=50)
    class_to_student = models.CharField("Класс", max_length=3)
    teacher_of_class = models.ForeignKey(Teacher, verbose_name='Классный руководитель', null=True, on_delete=models.SET_NULL)
    photo = models.ImageField("Фотография", upload_to='photoStudent/')
    achivement = models.TextField("Достижения")
    balls = models.PositiveIntegerField("Баллы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

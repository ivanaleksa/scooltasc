from django.db import models



class Teacher(models.Model):
    name = models.CharField("ФИО", max_length=50)
    rang = models.CharField("Должность", max_length=30)
    photo = models.ImageField("Фотография", upload_to='photoTeacher/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

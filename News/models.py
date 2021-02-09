from django.db import models


class New(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    image = models.ImageField("Изображение", upload_to='newsTitle/')
    text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикаций", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

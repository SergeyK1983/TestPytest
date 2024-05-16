from django.db import models


class CurrentModel(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    description = models.CharField(max_length=150, blank=True, null=True, verbose_name="Описание")
    count = models.IntegerField(verbose_name="Число")

    class Meta:
        verbose_name = 'Новая модель'
        verbose_name_plural = 'Новые модели'

    def __str__(self):
        return f"{self.id}-{self.name}"


class RelCurrent(models.Model):
    current = models.ForeignKey(to=CurrentModel, on_delete=models.CASCADE, related_name="current")
    text = models.CharField(max_length=155, verbose_name="Текст")

    class Meta:
        verbose_name = 'Зависимость'
        verbose_name_plural = 'Зависимости'

    def __str__(self):
        return f"{self.id}-{self.current}"

from django.db import models


class User(models.Model):
    From: models.TextField = models.TextField(
        verbose_name="Точка отправления", null=True, blank=False
    )
    To: models.TextField = models.TextField(
        verbose_name="Точка прибытия", null=True, blank=False
    )
    date: models.TextField = models.TextField(verbose_name="Дата", blank=False)
    time: models.TextField = models.TextField(
        verbose_name="Время", blank=False
    )
    count: models.IntegerField = models.IntegerField(
        verbose_name="Количество мест", blank=False, default=1
    )

    def get_absolute_url(self) -> str:
        return f"/taxi/main/{self.pk}/"

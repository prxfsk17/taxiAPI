from django.db import models


class User(models.Model):

    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=True)
    phone = models.TextField(verbose_name="Номер телефона", null=True, blank=True)

    def get_absolute_url(self)-> str:
        return f"/taxi/main/{self.pk}/"
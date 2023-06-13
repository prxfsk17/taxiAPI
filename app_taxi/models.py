from django.db import models


class User(models.Model):

    name = models.TextField(verbose_name="Имя пользователя", null=True, blank=True)
    phone = models.TextField(verbose_name="Номер телефона", null=True, blank=True)

    def get_absolute_url(self)-> str:
        return f"/taxi/main/{self.pk}/"

class AddressManager(models.Manager):
    pass
class Address(models.Model):
    objects = AddressManager()

    city = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TagManager(models.Manager):
    pass

class Tag(models.Model):
    objects = TagManager()

    label = models.TextField(unique=True)

    contacts = models.ManyToManyField(User)
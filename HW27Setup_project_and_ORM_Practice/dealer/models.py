from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(
        max_length=250,
    )
    e_mail = models.EmailField(
        max_length=50,
    )

    user = models.OneToOneField(
        USER_MODEL,
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        'dealer.City',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилери'


class City(models.Model):
    name = models.CharField(
        max_length=100,
    )

    country = models.ForeignKey(
        'dealer.Country',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    code = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'


class NewsLetter(models.Model):
    email = models.EmailField(
        max_length=100,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Лист'
        verbose_name_plural = 'Листи'

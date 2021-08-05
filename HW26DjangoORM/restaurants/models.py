from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    workers = models.ManyToManyField('restaurants.Workers')
    country = models.OneToOneField('restaurants.Country',on_delete=models.SET_NULL, null=True)
    city = models.OneToOneField('restaurants.City', on_delete=models.SET_NULL, null=True)
    menu = models.ManyToManyField('restaurants.Menu')

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторани'


class Workers(models.Model):
    POST_WAITER = 'waiter'
    POST_COOK = 'cook'
    POST_ADMINISTRATOR = 'administrator'

    POSITION_CHOICES = (
        (POST_WAITER, "Waiter"),
        (POST_COOK, "Cook"),
        (POST_ADMINISTRATOR, "Administrator"),
    )

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    post = models.CharField(max_length=25, choices=POSITION_CHOICES, blank=True)


    class Meta:
        verbose_name = 'Працівник'
        verbose_name_plural = 'Працівники'


class Country(models.Model):
    country = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'


class City(models.Model):
    city = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'


class Menu(models.Model):
    menu = models.CharField(max_length=255)
    food = models.TextField()
    food_price = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class Car(models.Model):
    ENGINE_TYPE_STRAIGHT = 'straight'
    ENGINE_TYPE_INLINE = 'inline'
    ENGINE_TYPE_FLAT = 'flat'
    ENGINE_TYPE_V = 'v'

    ENGINE_TYPE_CHOICES = (
        (ENGINE_TYPE_STRAIGHT, 'Straight engine'),
        (ENGINE_TYPE_INLINE, 'Inline Engine'),
        (ENGINE_TYPE_FLAT, 'Flat Engine'),
        (ENGINE_TYPE_V, 'V Engine')
    )

    POLLUTANT_CLASS_AA = 'a+'
    POLLUTANT_CLASS_A = 'a'
    POLLUTANT_CLASS_B = 'b'
    POLLUTANT_CLASS_C = 'c'
    POLLUTANT_CLASS_D = 'd'
    POLLUTANT_CLASS_E = 'e'
    POLLUTANT_CLASS_F = 'f'
    POLLUTANT_CLASS_G = 'g'

    POLLUTANT_CLASS_CHOICES = (
        (POLLUTANT_CLASS_AA, 'A+'),
        (POLLUTANT_CLASS_A, 'A'),
        (POLLUTANT_CLASS_B, 'B'),
        (POLLUTANT_CLASS_C, 'C'),
        (POLLUTANT_CLASS_D, 'D'),
        (POLLUTANT_CLASS_E, 'E'),
        (POLLUTANT_CLASS_F, 'F'),
        (POLLUTANT_CLASS_G, 'G'),
    )

    FUEL_TYPE_GASOLINE = 'gasoline'
    FUEL_TYPE_DIESEL = 'diesel'
    FUEL_TYPE_GAS = 'gas'
    FUEL_TYPE_ELECTRICITY = 'electricity'

    FUEL_TYPE_CHOICES = (
        (FUEL_TYPE_GASOLINE, 'Gasoline'),
        (FUEL_TYPE_DIESEL, 'Diesel'),
        (FUEL_TYPE_GAS, 'Gas'),
        (FUEL_TYPE_ELECTRICITY, 'Electricity'),
    )

    STATUS_PENDING = 'pending'
    STATUS_PUBLISH = 'publish'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending Car Sell'),
        (STATUS_PUBLISH, 'Published'),
        (STATUS_SOLD, 'Sold'),
        (STATUS_ARCHIVED, 'Archived'),
    )

    GEAR_CASE_MANUAL = 'manual transmission'
    GEAR_CASE_AUTOMATIC = 'automatic transmission'

    GEAR_CASE_CHOICES = (
        (GEAR_CASE_MANUAL, 'Manual Transmission'),
        (GEAR_CASE_AUTOMATIC, 'Automatic Transmission'),
    )

    color = models.ForeignKey(
        'car.Color',
        on_delete=models.CASCADE,
    )

    dealer = models.ForeignKey(
        'dealer.Dealer',
        on_delete=models.CASCADE,
    )
    model = models.ForeignKey(
        'car.Model',
        on_delete=models.CASCADE,
    )

    engine_type = models.CharField(
        max_length=50,
        choices=ENGINE_TYPE_CHOICES,
        default=ENGINE_TYPE_STRAIGHT,
    )

    pollutant_class = models.CharField(
        max_length=2,
        choices=POLLUTANT_CLASS_CHOICES,
        default=POLLUTANT_CLASS_AA,
    )

    price = models.PositiveIntegerField(
        default=0,
    )

    fuel_type = models.CharField(
        max_length=30,
        choices=FUEL_TYPE_CHOICES,
        default=FUEL_TYPE_GASOLINE,
    )

    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )

    doors = models.PositiveIntegerField(
        default=4,
    )

    capacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    gear_case = models.CharField(
        max_length=255,
        choices=GEAR_CASE_CHOICES,
        default=GEAR_CASE_MANUAL,
    )

    number = models.CharField(
        max_length=20,
    )

    slug = models.SlugField(
        max_length=100,
    )

    sitting_place = models.PositiveIntegerField(
        default=5,
    )

    first_registration_date = models.DateTimeField(
        auto_now_add=True,
    )

    engine_power = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машини'


class Color(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Колір'
        verbose_name_plural = 'Кольори'


class Model(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    brand = models.ForeignKey(
        'car.Brand',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'


class Brand(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'


class Picture(models.Model):
    position = models.IntegerField()
    metadata = models.TextField(
        null=True,
        blank=True,
    )
    url = models.ImageField(
        upload_to='pictures',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.url.name

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'


class Property(models.Model):
    CATEGORY_PASSANGER = 'passanger'
    CATEGORY_TRUCK = 'truck'
    CATEGORY_BUS = 'bus'

    CATEGORY_CHOICES = (
        (CATEGORY_PASSANGER, 'Passanger car'),
        (CATEGORY_TRUCK, 'Truck'),
        (CATEGORY_BUS, 'Bus'),
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_PASSANGER,
    )

    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class CarProperty(models.Model):
    property = models.ForeignKey(
        'car.Property',
        on_delete=models.CASCADE,
    )

    car = models.ForeignKey(
        'car.Car',
        on_delete=models.CASCADE,
    )
import factory
from . import models


class CarFactory(factory.Factory):
    class Meta:
        model = models.Car

    color = 'White'
    dealer = 'Ben'
    model = 'Tesla'
    engine_type = 'Inline engine'
    pollutant_class = 'A+'
    price = 100000
    fuel_type = 'Electricity'
    status = 'Sold'
    doors = 4


class ColorFactory(factory.Factory):
    class Meta:
        model = models.Color

    name = 'White'


class ModelFactory(factory.Factory):
    class Meta:
        model = models.Model

    brand = 'Tesla'



import factory
from . import models


class DealerFactory(factory.Factory):
    class Meta:
        model = models.Dealer

    e_mail = 'ben123@gmail.com'
    title = 'Dealer1'


class CityFactory(factory.Factory):
    class Meta:
        model = models.City

    name = 'Kharkiv'


class CountryFactory(factory.Factory):
    class Meta:
        model = models.Country

    name = 'Ukraine'

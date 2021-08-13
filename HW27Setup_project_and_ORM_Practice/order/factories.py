import factory
from . import models


class OrderFactory(factory.Factory):
    class Meta:
        model = models.Order

    first_name = 'Igor'
    last_name = 'Vasilenko'
    email = 'igorvasilenko@gmail.com'
    phone = '0685694332'

from django.db import models

class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_ACCEPT = 'accept'
    STATUS_IN_PROGRESS = 'in-progress'
    STATUS_CANCEL = 'cancel'
    STATUS_COMPLETE = 'complete'

    STATUS_CHOICES =(
        (STATUS_NEW, 'New order'),
        (STATUS_ACCEPT, 'Accept'),
        (STATUS_IN_PROGRESS, 'In-progress'),
        (STATUS_CANCEL, 'Cancel'),
        (STATUS_COMPLETE, 'Complete'),
    )

    car = models.ForeignKey(
        'car.Car',
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        max_length=100,
    )

    phone = models.IntegerField(
        blank=True,
    )

    message = models.TextField()

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
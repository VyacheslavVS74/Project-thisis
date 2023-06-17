from django.db import models

from django.db import models
from portfolio.models import Works


class StatusCrm(models.Model):

    status_name = models.CharField(max_length=150, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_works = models.ForeignKey(Works, on_delete=models.CASCADE, verbose_name='Работа')
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    # order_work = models.CharField(max_length=250, verbose_name='Изделие', null=True)
    order_name = models.CharField(max_length=50, verbose_name='Имя')
    order_phone = models.CharField(max_length=50, verbose_name='Телефон')
    order_email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='Email')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя Банка')
    capital_sum = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Капитал банка')
    credit_sum = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма кредита')
    client = models.ManyToManyField('Client', verbose_name='Клиент')
    credit_name = models.ForeignKey('Credit', on_delete=models.CASCADE, verbose_name='Наименование кредита')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'


class Credit(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование кредита')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наименование кредита'
        verbose_name_plural = 'Наименование кредита'

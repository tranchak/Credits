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


class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя клиента', help_text='Введите имя клиента')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия клиента', help_text='Введите фамилию клиента')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    sum_credit = models.DecimalField(max_digits=1000000, decimal_places=2, verbose_name='Сумма кредита')
    credit_term = models.DateField(blank=False, verbose_name='Срок кредита')
    percent = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Процент кредита')
    worker = models.BooleanField(default=False, verbose_name='Работник банка или нет')

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

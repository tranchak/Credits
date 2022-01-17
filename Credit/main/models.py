from django.db import models

# Create your models here.
class Client(models.Model):
    first_name=models.CharField(max_length=100, verbose_name='Имя клиента', help_text='Введите имя клиента')
    last_name=models.CharField(max_length=100, verbose_name='Фамилия клиента',help_text='Введите фамилию клиента')
    birthday=models.DateField(null=True, blank=True,verbose_name='Дата рождения')
    sum_credit=models.DecimalField(max_digits=1000000,decimal_places=2,verbose_name='Сумма кредита')
    credit_term=models.DateField(blank=False,verbose_name='Срок кредита')
    percent=models.DecimalField(max_length=3,max_digits=2, verbose_name='Процент кредита')
    worker=models.BooleanField(default=False,verbose_name='Работник банка или нет')

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'
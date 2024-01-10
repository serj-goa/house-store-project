from django.db import models as m

from houses.models import House


class Order(m.Model):
    house = m.ForeignKey(House, verbose_name='Дом', on_delete=m.CASCADE)
    name = m.CharField(verbose_name='Имя', max_length=50)
    phone = m.CharField(verbose_name='Телефон', max_length=50)
    date = m.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name

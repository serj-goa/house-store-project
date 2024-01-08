from django.db import models as m


class House(m.Model):
    name = m.CharField(verbose_name='Название', max_length=50)
    price = m.IntegerField(verbose_name='Цена')
    description = m.TextField(verbose_name='Описание')

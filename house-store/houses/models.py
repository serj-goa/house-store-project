from django.db import models as m


class House(m.Model):
    name = m.CharField(verbose_name='Название', max_length=50)
    price = m.IntegerField(verbose_name='Цена')
    description = m.TextField(verbose_name='Описание')
    photo = m.ImageField(verbose_name='Фото', upload_to='houses/photos', default='', blank=True)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

        ordering = 'name', 'price'

    def __str__(self):
        return self.name

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='марка')
    model = models.CharField(max_length=50, verbose_name='модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()
    review_count.short_description = 'Количество обзоров'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Review(models.Model):
    car = models.ForeignKey(Car, verbose_name='машина', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = 'обзор'
        verbose_name_plural = 'обзоры'
from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import User
from django.utils import timezone
from django.utils.timesince import timesince


class Service(models.Model):
    name = models.CharField("Название сервиса", max_length=50)
    full_price = models.PositiveIntegerField("Полная цена")

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return f'{self.name} - {self.full_price}'


class Plan(models.Model):
    PLAN_TYPES = (
        ("full", "Полный"),
        ("student", "Студенческий"),
        ('discount', 'Скидка')
    )
    plan_types = models.CharField("Тарифный план", choices=PLAN_TYPES, max_length=15)
    description = models.TextField('Описание', max_length=400)
    discount_percent = models.PositiveIntegerField("Скидка", default=0, validators=[
        MaxValueValidator(100)
    ])

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'

    def __str__(self):
        return f'{self.plan_types} - {self.discount_percent}'


class Subscription(models.Model):
    client = models.ForeignKey(User, related_name="subscriptions", on_delete=models.CASCADE, verbose_name="Пользователь")
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.CASCADE, verbose_name="Сервис")
    plan = models.ForeignKey(Plan, related_name="subscriptions", on_delete=models.CASCADE, verbose_name="План")
    description = models.TextField('Описание', max_length=600)
    date_joined = models.DateTimeField("Дата", default=timezone.now)

    """функция времени"""
    def created_at_formatted(self):
       return f' Был: {timesince(self.date_joined)} назад'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.client} - {self.service} - {self.plan}'

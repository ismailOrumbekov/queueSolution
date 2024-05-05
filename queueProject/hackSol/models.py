from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Customer(models.Model):
    FullName = models.CharField(max_length=100, verbose_name="Полное имя")
    Age = models.IntegerField(verbose_name="Возраст")


class Services(models.Model):
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    ServiceName = models.CharField(max_length=100, verbose_name="Название услуги")
    AverageTime = models.IntegerField(verbose_name="Среднее время выполнения")


class Worker(models.Model):
    NickName = models.ForeignKey(User)
    FullName = models.CharField(max_length=100, verbose_name="Полное имя")
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Service = models.ForeignKey(Services, on_delete=models.CASCADE)


class Organization(models.Model):
    OrganizationName = models.CharField(max_length=100)
    NumberOfService = models.IntegerField(verbose_name="Количество услуг")
    NumberOfWorkers = models.IntegerField(verbose_name="Количество работников")
    MaxNumberOfCustomersPerDay = models.IntegerField(verbose_name="Максимальнок количество")
    Address = models.CharField(max_length=200, verbose_name="Адрес")


class Request(models.Model):
    Service = models.ForeignKey(Services, on_delete=models.CASCADE)
    StartTime = models.DateField(default=datetime.now(), verbose_name="Время начала услуги")
    EndTime = models.DateField(null=True, verbose_name="Окончание услуги")
    IsFinished = models.BooleanField(default=False, verbose_name="Заказ обработан")
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
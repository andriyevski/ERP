from django.urls import reverse
from django.db import models

# Create your models here.

class Client(models.Model):
    id_dep_client = models.TextField(max_length=100, verbose_name="ID департаменту та клієнта")
    name_client = models.TextField(max_length=100, verbose_name="ПІБ клиента")

    def __str__(self):
        return self.name_client

    class Meta:
        verbose_name = 'ID департаменту та клієнта'
        verbose_name_plural = 'ID департаменту та клієнтів'


class Project_Num(models.Model):
    id_dep_client = models.TextField(max_length=100, verbose_name="ID департаменту та клієнта")
    id_project = models.TextField(max_length=100,verbose_name='ID проекту')

    def get_absolute_url(self):
        return reverse('form', kwargs = {"id_project": self.pk})
    
    def __str__(self):
        return self.id_project

    class Meta:
        verbose_name = 'Проект №'
        verbose_name_plural = 'Проект №'
        ordering = ['-id_project']
from django.db import models
# Create your models here.

class City(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    def __str__(self):
        return self.nombre

class Person(models.Model):
    nombres = models.CharField(max_length=200, blank=False, null=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL,blank=True,null=True,)
    def __str__(self):
        return self.nombres

class Book(models.Model):
    titulo=models.CharField(max_length=200, blank=False, null=False)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

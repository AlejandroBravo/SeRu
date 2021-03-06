# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
	telefono_contacto = models.CharField(max_length=9,null=False,default='000000000')	

class Post(models.Model):
	nombre_post = models.CharField(max_length=50,null=False,default='Vendo Vehiculo')
	usuario_creador = models.ForeignKey('User',on_delete=models.CASCADE)
	vehiculo_id = models.ForeignKey('Vehiculo',on_delete=models.CASCADE)
	ubicacion = models.CharField(max_length=100,null=False)
	descripcion = models.TextField(null=False)
	precio = models.PositiveIntegerField(null=False)
	
	def __unicode__(self):
		return self.nombre_post

class Vehiculo(models.Model):
	clase_vehiculo = models.CharField(null=False,max_length=100)
	marca = models.CharField(null=False,max_length=100)
	modelo = models.TextField(null=False)
	tipo = models.TextField(null=False)
	
	def __unicode__(self):
		return self.modelo

	
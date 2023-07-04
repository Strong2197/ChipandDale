from django.conf import settings
from django.db import models
from django.utils import timezone
from django.shortcuts import redirect
import os

class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name="Заголовок")
	text = models.TextField(verbose_name="Текст")
	published_date = models.DateTimeField(blank = True, null = True, verbose_name="Дата публікації")
	image = models.ImageField(null=True, verbose_name="Фото", max_length=200)

	class Meta():
		verbose_name = 'Новина'
		verbose_name_plural = "Новини"


	def publish(self):
		self.published_date=timezone.now()
		self.save

	def __str__(self):
		return self.title

class Menu(models.Model):
	price = models.CharField(max_length=100, verbose_name="Ціна")
	dish = models.CharField(max_length=100, verbose_name="Страва")

	class Meta():
		verbose_name = 'Меню'
		verbose_name_plural = "Меню"


	def publish(self):
		self.save

	def __str__(self):
		return self.dish + " " + self.price
class Attracs(models.Model):
	price = models.CharField(max_length=100, verbose_name="Ціна")
	name = models.CharField(max_length=100, verbose_name="Назва")
	image = models.ImageField(null=True, verbose_name="Фото", max_length=200)

	class Meta():
		verbose_name = 'Атракціони'
		verbose_name_plural = "Атракціони"


	def publish(self):
		self.save

	def __str__(self):
		return self.name

class MultipleImage(models.Model):
	postid = models.CharField(null=True, max_length=100, verbose_name="До новини")
	images = models.ImageField(null=True, verbose_name="Фото", max_length=200)

	class Meta():
		verbose_name = 'Фото до новини'
		verbose_name_plural = "Фото до новини"

	def publish(self):
		self.save

	def __str__(self):
		return self.postid



from django.conf import settings
from django.db import models
from django.utils import timezone
from django.shortcuts import redirect
import os

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateTimeField(blank = True, null = True)
	image = models.ImageField(null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save

	def __str__(self):
		return self.title

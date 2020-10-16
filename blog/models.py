from django.db import models

from django.db import models

class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField()

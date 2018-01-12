
from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
	data = models.TextField()
	user = models.ForeignKey(User)
	# keywords = models.CharField(max_length=500)

class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=255, blank=True)
	#uploaded_at = models.DateTimeField(auto_now_add=True)

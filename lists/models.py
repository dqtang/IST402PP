from django.db import models

# Create your models here.
class Courses(models.Model):
    text = models.TextField(default = '')
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   avatar = models.ImageField(upload_to='static/images')
   username = models.CharField(max_length=12)

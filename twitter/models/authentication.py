from django.db import models
from . import User


class Authentication(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)

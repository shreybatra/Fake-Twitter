from django.db import models
from . import User


class Tweet(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	tweet_text = models.CharField(max_length=500)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	is_retweet = models.BooleanField(default=False)
	retweets = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
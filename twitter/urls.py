from twitter.views import home, user_management, user_login, user_logout, follow_user, unfollow_user, tweet
from django.urls import path, include

urlpatterns = [
    path('', home),
    path('user', user_management),
    path('authenticate/_login', user_login),
    path('authenticate/_logout', user_logout),
    path('user/_follow', follow_user),
    path('user/_unfollow', unfollow_user),
    path('tweet', tweet)
]

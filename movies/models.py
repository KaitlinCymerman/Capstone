from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Movies(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(blank=False)
    about = models.CharField(max_length=1000)
    image = models.CharField(max_length=2000)
    watchlist = models.ManyToManyField(User, blank=True, default=None, related_name="watch_listing")

    def __str__(self):
        return self.title

class Reviews(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="movie_review")
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="review")
    timestamp = models.DateTimeField(auto_now_add=True)
    review = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)




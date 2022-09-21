from django.db import models

# Create your models here.
class MyWatchlistItem(models.Model):
    status_watched_film = models.BooleanField()
    title_film = models.CharField(max_length=50)
    rating_film = models.CharField(max_length=50)
    release_date_film = models.TextField()
    review_film = models.TextField()

from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    poster_path=models.TextField()
    overview=models.TextField()
    release_date = models.DateTimeField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="movie_genres")


class Score(models.Model):
    # user = models.IntegerField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField()
    # score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
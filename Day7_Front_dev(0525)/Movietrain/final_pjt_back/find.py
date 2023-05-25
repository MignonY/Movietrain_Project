import json
import requests

# 다른 이름의 .py를 실행하려면 아래와 같이 셋팅을 해주어야 함
#############################################
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt.settings')
django.setup()
#############################################

from movies.models import Movie
from movies.serializer import MovieListSerializer

movies = Movie.objects.filter(title__icontains='어벤')
serializer = MovieListSerializer(movies, many=True)
for movie in movies:
    print(movie.title)
    print(movie.id)

for i in serializer:
    print(i)
# for movie in movies:
#     print(movie)
# print(movies)
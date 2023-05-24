import json
import requests

# 다른 이름의 .py를 실행하려면 아래와 같이 셋팅을 해주어야 함
#############################################
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt.settings')
django.setup()
#############################################

from movies.models import Genre, Movie

def get_genre():
    genres = Genre.objects.all()
    if len(genres)==0: 
        base_url = 'https://api.themoviedb.org/3'
        path = '/genre/movie/list'
        params = {
            'api_key' : '8fbf533cae830be37207c14a5de525f7',
            'language' : 'Ko',
        }
        res_genre = requests.get(base_url + path, params = params)
        genre_content = res_genre.content
        genre_list = json.loads(genre_content.decode('utf-8'))

        genres_data=genre_list['genres']
        print(genres_data)

        for datum in genres_data:
            genre = Genre(
                id = datum["id"],
                name = datum["name"],
            )
            genre.save()
    return

def get_pop():
    movies = Movie.objects.all()
    if len(movies)==0:
        base_url = 'https://api.themoviedb.org/3'
        path = '/movie/popular'
        API_KEY = '8fbf533cae830be37207c14a5de525f7'
        for i in range(1, 30):
            params = {
                'api_key' : API_KEY,
                'language' : 'ko',
                'page' : f'{i}',
            }
            res = requests.get(base_url+path, params=params)
            data = res.json()
            movies = data['results']
            for datum in movies:
                movie = Movie(
                    id = datum['id'],
                    title = datum['title'],
                    poster_path = datum['poster_path'],
                    overview = datum['overview'],
                    release_date = datum['release_date'],
                    vote_average = datum['vote_average'],
                    vote_count = datum['vote_count'],
                )
                movie.save()
            break
    return

# 실행
get_genre()
get_pop()
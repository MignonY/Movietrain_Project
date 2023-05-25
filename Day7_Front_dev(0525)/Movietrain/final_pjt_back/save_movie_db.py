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

# page 10까지 db저장하기

for i in range(21, 500):
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page={i}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM"
    }

    response = requests.get(url, headers=headers)
    movie_content = response.content
    movie_list = json.loads(movie_content.decode('utf-8'))
    data = movie_list['results']

    for datum in data:
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
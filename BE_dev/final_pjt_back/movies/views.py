from .models import Movie, Score
from . serializer import MovieListSerializer, MovieDetailSerializer, MovieScoreSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        movies = movie.order_by('-vote_count')
        serializer = MovieListSerializer(movies[:24], many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def score_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method=='POST':
        serializer = MovieScoreSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie,user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def score_detail(request, score_pk):
    score = Score.objects.get(pk =score_pk)
    if request.method =='GET':
        serializer = MovieScoreSerializer(score)
        return Response(serializer.data)

    elif request.method =='DELETE':
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method =='PUT':
        serializer = MovieScoreSerializer(score, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    


@api_view(['GET'])
def score_list(request):
    scores = get_list_or_404(Score)
    serializer = MovieScoreSerializer(scores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search(request, title):
    if request.method =='GET':
        print(title)
        print(request)
        search = Movie.objects.filter(title__contains=title)
        print(search)
        serializer = MovieListSerializer(search, many=True)
        return Response(serializer.data)
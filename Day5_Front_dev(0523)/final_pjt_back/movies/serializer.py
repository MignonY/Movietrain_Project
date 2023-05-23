from rest_framework import serializers
from .models import Movie, Genre, Score

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # exclude = ['id', ]
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields='__all__'

class MovieScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields='__all__'


    # def create(self, validated_data):
    #     # Get the star rating from the validated_data
    #     star_rating = validated_data.pop('star_rating', None)

    #     # Create a new Score instance with the star rating
    #     score = Score.objects.create(star_rating=star_rating, **validated_data)

    #     return score

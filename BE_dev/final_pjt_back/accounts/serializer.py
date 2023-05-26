from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.serializer import PostListSerializer
from movies.serializer import MovieScoreSerializer
from community.models import Post
from movies.models import Score
User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    # like_posts = PostListSerializer(many=True)
    post_set = serializers.SerializerMethodField()
    score_set = serializers.SerializerMethodField()

    # get_ method를 통해 ORM으로 data serializer
    def get_post_set(self, user):
        posts = Post.objects.filter(user=user)
        serializer = PostListSerializer(posts, many=True)
        return serializer.data

    def get_score_set(self, user):
        scores= Score.objects.filter(user=user)
        serializer = MovieScoreSerializer(scores, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ['id','username', 'followers', 'followings', 'post_set', 'score_set',]




class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



        
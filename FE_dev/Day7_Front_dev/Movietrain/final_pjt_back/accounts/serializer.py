from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.serializer import PostListSerializer
from community.models import Post
User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    like_posts = PostListSerializer(many=True)
    post_set = serializers.SerializerMethodField()

    def get_post_set(self, user):
        posts = Post.objects.filter(user=user)
        serializer = PostListSerializer(posts, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ['id','username', 'followers', 'followings', 'post_set','like_posts' ,]




class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



        
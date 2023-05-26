from rest_framework import serializers
from .models import Post, Comment, Reply
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','user','title','content')
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'content', 'created_at')


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('post', 'comment', 'content', 'created_at')

class PostDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    reply_set = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('user','id','title', 'content','created_at','updated_at','comment_set', 'comment_count', 'reply_set')
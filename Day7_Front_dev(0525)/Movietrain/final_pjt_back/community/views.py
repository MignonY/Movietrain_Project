from django.shortcuts import render
from .models import Post, Comment, Reply
from accounts.models import User
from .serializer import PostListSerializer, PostDetailSerializer, CommentSerializer, ReplySerializer
from rest_framework.response import Response

# 인증 기능 추가
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


#http request
from rest_framework import status  # 상태 알려주는 status
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view


# 리스트 불러오기, post 생성하기
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == 'GET':
        post_list = Post.objects.all()
        serializer = PostListSerializer(post_list, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostListSerializer(data=request.data)
        print('#################')
        print(request.user)
        # USER = User.objects.get(username=request.user)
        # print(USER.id)
        print('#################')
        
        if serializer.is_valid(raise_exception=True):
            
            serializer.save(user=request.user)
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Post Detail
@api_view(['GET','DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'GET':
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
    
    elif request.method =='DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = PostDetailSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# Comment
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

@api_view(['GET','DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    

@api_view(['POST'])
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def reply_list(request):
    if request.method == 'GET':
        reply = Reply.objects.all()
        serializer = CommentSerializer(reply, many=True)
        return Response(serializer.data)


@api_view(['GET','DELETE', 'PUT'])
def reply_detail(request, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(reply)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        reply.delete()

    elif request.method == 'PUT':
        serializer = CommentSerializer(reply, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def reply_create(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post, comment=comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

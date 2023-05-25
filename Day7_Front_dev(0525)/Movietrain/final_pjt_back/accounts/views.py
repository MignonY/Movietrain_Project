from django.shortcuts import render
from .serializer import UserProfileSerializer, UserDetailSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.authtoken.models import Token
from django.http import JsonResponse

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_profile(request, user_pk):
#     if request.method =='GET':
#         user = User.objects.get(pk=user_pk)
#         serializer  = UserProfileSerializer(user)

#         return Response(serializer.data)
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def user_profile(request):
    username = User.objects.get(username=request.user.
    username)
    # username = get_list_or_404(User, username=username)
    if request.method =='GET':
        serializer  = UserProfileSerializer(username)
        return Response(serializer.data)

    # if request.method =='DELETE':
    #     username.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # if request.method == 'PUT':
    #     serializer = UserDetailSerializer(username, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


@api_view(['GET'])
def get_user_profile(request, username):
    print('#####################')
    print('username:',username)
    print('request:',request.user)

    print('#####################')
    username = User.objects.get(username=username)
    # followings = User.followings.get(sername=username)

    if request.method =='GET':
        serializer  = UserProfileSerializer(username)
        return Response(serializer.data)

# request.user => user의 instance를 말하는거고요
#     로그인을 했을 때 => db안의 사람
#     로그인ㅇ르안했을때 => anonymous user를 말함. => user 입장에서의 null
# request.user.username => 사람의 이름

# vue
# axios( url, headers = {token }) => 토큰을 가지고 로그인을 하게 되면
# url => view로 통과 middleware

# user가 검색을 

# vue는 request를 보내고 response를 받고
#     request에다가 paramse, query라는 녀석을 사용해서 dajgno에 추가적인 데이터를 넘겨줄 수 있죠
#     movies/?key=value&key=value => django에서 key-value 사용 가능
#     profile/:username => django에서 username을 변수로 사용 가능

# django는 request를 받아다가 response를 보내죠

@api_view(['POST'])
def follow(request, username, yourname):
    you = User.objects.get(username=yourname)
    me = User.objects.get(username=username)

    if me in you.followers.all():
        you.followers.remove(me)
        return Response("언팔로우 했습니다.", status=status.HTTP_200_OK)
    
    else:
        you.followers.add(me)
        return Response("팔로우 했습니다.", status=status.HTTP_200_OK)
"""final_pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),

    #회원가입 
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('user/', include('accounts.urls')),
    path('accounts/', include('dj_rest_auth.urls')),

    #path('accounts/', include('dj_rest_auth.urls')),
    # 소셜 인증 로그인 
    #path("accounts/", include("allauth.urls")),

    #커뮤니티
    path('community/', include('community.urls')),
    
    # 영화
    path('movies/', include('movies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
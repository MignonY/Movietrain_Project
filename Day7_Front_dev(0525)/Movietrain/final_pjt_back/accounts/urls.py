from django.urls import path, include
from . import views

urlpatterns = [
    path('userid/', views.user_profile),
    path('profile/<str:username>/', views.get_user_profile),
    path('profile/<str:username>/<str:yourname>/', views.follow),
]
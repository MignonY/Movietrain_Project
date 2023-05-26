from django.urls import path, include
from . import views

urlpatterns = [
    path('userid/', views.user_profile),
    path('<int:userid>/', views.get_user_profile),
    path('profile/<int:username>/<int:yourname>/', views.follow),
]
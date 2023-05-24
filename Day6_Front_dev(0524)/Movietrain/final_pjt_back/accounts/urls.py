from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:username>/', views.user_profile),
    path('userid/', views.get_user_id),
]

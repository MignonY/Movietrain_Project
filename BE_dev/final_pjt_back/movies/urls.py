from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/score/', views.score_create),
    path('score/<int:score_pk>/', views.score_detail),
    path('score/', views.score_list),
    path('search/<str:title>', views.search),

]

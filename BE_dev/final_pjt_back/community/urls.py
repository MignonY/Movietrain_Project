from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('<int:post_pk>/',views.post_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:post_pk>/comment/', views.comment_create),
    path('<int:post_pk>/<int:comment_pk>/reply/', views.reply_create),
    path('reply/', views.reply_list),
    path('reply/<int:reply_pk>/', views.reply_detail),
]


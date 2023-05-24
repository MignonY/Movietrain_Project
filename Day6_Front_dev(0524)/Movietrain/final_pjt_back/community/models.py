from django.db import models


# Create your models here.
class Post(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_comments')

class Reply(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_comments')
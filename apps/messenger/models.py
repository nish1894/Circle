from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ChatMessage(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.message[:20]}..."

    class meta:
        ordering = ['-created']

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=255, unique = True)
    users_online = models.ManyToManyField(User, related_name='online_users', blank = True)


    def __str__(self):
        return self.group_name

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup,related_name='group_message' ,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length = 300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} : {self.body}'

    class Meta:
        ordering = ['-created']

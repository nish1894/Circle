from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank = True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank = True)


    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self. display_name:
            return self.display_name
        return self.user.username


    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'



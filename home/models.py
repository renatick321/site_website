from django.db import models
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/', default='images/logo.png')
 
    def __str__(self):
        return self.title



class User(AbstractUser):
    image = models.ImageField(upload_to='images/', default='images/logo.png', blank=True)
    location = models.CharField(max_length=30, blank=True, default='Neverland', null=True)
    birth_date = models.DateField(null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
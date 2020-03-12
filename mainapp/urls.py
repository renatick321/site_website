
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.comments_create, name='comments_create'),
    path('create/', views.article_create, name='article_create'),
    path('delete/<int:article_id>/', views.article_delete, name='article_delete'),
    path('redact/<int:article_id>/', views.fix_article, name='fix_article'),
#    path('registration/', views.registration, name='registration')
]

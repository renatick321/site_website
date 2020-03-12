from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.home, name='home'),
	path('registration/', views.registration, name='registration'),
	path('login/', views.user_login, name='user_login'),
	path('logout/', views.user_logout, name='user_logout'),
	path('photo/', views.photo, name='photo'),
	path('fix_account/', views.fix_account, name='fix_account'),
	path('id<int:account_id>/', views.account, name='account')
]
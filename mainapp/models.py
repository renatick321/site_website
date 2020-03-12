import datetime
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from home.models import User
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	pub_date = models.DateTimeField('Дата публикауции', default=timezone.now)
	author_name = models.ForeignKey(User, on_delete = models.CASCADE)
	image = models.ImageField('Изображение', upload_to='images/', default='images/logo.png')
	description = models.CharField('Описание', max_length=100)

	def __str__(self):
		return self.article_title

	def published_res(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	comment_text = models.CharField(max_length = 50000)
	pub_date = models.DateTimeField(default = timezone.now)
	
	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'


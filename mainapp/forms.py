from .models import  Comment, Article
from django import forms



class CommentForm(forms.Form):
	comment_text = forms.CharField(widget=forms.Textarea)


class ArticleCreationForm(forms.ModelForm):
	
	class Meta:
		model = Article
		fields = ['article_text', 'article_title']
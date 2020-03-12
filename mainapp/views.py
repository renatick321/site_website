from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Comment, Article
from .forms import CommentForm, ArticleCreationForm
from home.models import User


def index(request):
	articles_list = Article.objects.order_by('-pub_date') #[:15]'эта переменная закидывается в шаблонизатор'
	return render(request, 'mainapp/articles_list.html', {'articles_list': articles_list, 'username': request.user})

def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
        comments= Comment.objects.filter(article=article_id)
    except:
        raise Http404('Статья не найдена')

    return render(request, 'mainapp/typ_page.html', {'article':a, 'comments': comments, 'username': request.user})

def comments_create(request, article_id):
    if request.user.is_authenticated:
        author_name = request.user
    else:
        author_name = 'Guest'
    try:

        a = Article.objects.get(id=article_id)
        comments= Comment.objects.filter(article=article_id)[::-1]
        articles = article_id
    except:
        raise Http404('Статья не найдена')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author_name_id = request.user.id
            comment.comment_text = form.cleaned_data['comment_text']
            comment.article_id = articles
            comment.save()
            return redirect('/article/' + str(article_id) + '/')
    else:
        form = CommentForm()
    comments= Comment.objects.filter(article=article_id)[::-1]
    return render(request, 'mainapp/typ_page.html', {'article':a, 'comments': comments, 'username': request.user, 'author_name': author_name})


def article_create(request):
    author_name = request.user
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return render(request, 'mainapp/big_message.html', {'message': 'Вы не зарегестрированны', 'username': request.user})
    elif request.method == 'POST':
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            article = Article()
            article.article_title = form.cleaned_data['article_title']
            article.article_text = form.cleaned_data['article_text']
            article.author_name_id = request.user.id
            article.save()
            return redirect('/')
    return render(request, 'mainapp/article_create.html', {'author_name': author_name, 'username': request.user})

def article_delete(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        if not article.author_name_id == request.user.id and request.user.id != 0:
            raise Http404('Не найдено')
        article.delete()
    except:
        raise Http404('Не найдено')
    return redirect('/id{}/'.format(request.user.id))


def fix_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        if not article.author_name_id == request.user.id and request.user.id != 0:
            raise Http404('Не найдено')
        a = {'author_name': article.author_name, 'username': request.user, 'text': article.article_text, 'title': article.article_title}
        if request.method == 'POST':
            form = ArticleCreationForm(request.POST)
            if form.is_valid():
                article = Article.objects.get(id=article_id)
                article.article_title = form.cleaned_data['article_title']
                article.article_text = form.cleaned_data['article_text']
                article.author_name_id = request.user.id
                article.save()
                return redirect('/id{}/'.format(request.user.id))
        return render(request, 'mainapp/article_create.html', a)
    except:
        raise Http404('Не найдено')
    return redirect('/id{}/'.format(request.user.id))
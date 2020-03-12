from django.shortcuts import render, redirect
from .forms import RegForm, LoginForm, FixAccountForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Post, User
from mainapp.models import Article

# Create your views here.
def home(request):
	return render(request, 'home/homepage.html', {'username': request.user})

def registration(request):
	message = ''
	template = 'home/registration.html'
	if request.user.is_authenticated:
		template = 'home/big_message.html'
		message = 'Вы уже вошли'
	elif request.method == 'POST':
		form = RegForm(request.POST)
		print(form.is_valid)
		if form.is_valid():
			form.save()
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password1'])
			login(request, user)
			return redirect('/')
		else:
			form = RegForm(request.POST)
			errors = form.errors.as_data()
			messages = [i for i in errors]
			message = str(errors[messages[-1]])
			first = message.find("'") + 1
			second = message.rfind("'") - 1
			message = message[first:second]
	return render(request, template, {'message': message, 'username': request.user})
#НЕ ТРОГАЙ, ВСЁ ЗАКОНЧЕНО


def user_login(request):
	message = ''
	template = 'home/login.html'
	if request.user.is_authenticated:
		print(111111)
		print(request.user, 22)
		template = 'home/big_message.html'
		message = 'Вы уже вошли'
	elif request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			if cd['username'] is None:
				print(request.user)
			print(request.user, 11)
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				login(request, user)
				request.user = 'renat'
				print(request.user, 22)
				return redirect('/')
			else:
				message = 'Такого пользователя не существует'
		else:
			message = 'Введите данные заново'
			
			
	return render(request, template, {'message': message, 'username': request.user})#




def user_logout(request):
	logout(request)
	return redirect('/')


#def account(request):
#	if not request.user.is_authenticated:
#		raise Http404('Страница не найдена')
#	print(11111)
#	user = User.objects.get(username=request.user)
#	return render(request, 'home/account.html', {'username': request.user, 'user': user})

def photo(request):
	print(request.user)
	objects_list = Post.objects.all()
	return render(request, 'home/photo.html', {'object_list': objects_list})


def fix_account(request):
	print(111)
	user = User.objects.get(username=request.user)
	if not request.user.is_authenticated:
		raise Http404('Page do not found')
	elif request.method == 'POST':
		print(2222)
		form = FixAccountForm(request.POST, request.FILES)
		print('Печалька')
		if form.is_valid:
			print('класс')
			print(form)
			cd = form.cleaned_data
			user.username = cd.get('username')
			user.email = cd.get('email')
			if bool(cd.get('birth_date')):
				user.birth_date = cd.get('birth_date')
			user.location = cd.get('location')
			user.about_me = cd.get('about_me')
			if bool(cd.get('image')):
				user.image = cd.get('image')
			user.save()
			return redirect('/id{}/'.format(request.user.id))
	return render(request, 'home/fix_account.html', {'username': request.user, 'user': user,})


def account(request, account_id):
	try:
		Bool = False
		user = User.objects.get(id = account_id)
		l = Article.objects.filter(author_name = account_id)
		if str(request.user) == str(user.username):
			Bool = True
	except:
		raise Http404()
	return render(request, 'home/account.html', {'username': request.user, 'user': user, 'list': l, 'Bool': Bool})


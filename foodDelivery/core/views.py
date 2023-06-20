from django.shortcuts import render,redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from items.models import Item, Category
def index(request):
    items = Item.objects.filter(sold_out=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'cateogories' : categories,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form' : form,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            form = LoginForm()
            messages.warning(request, 'Your username or password is incorrect. Please try again.')
        
    else:
        form = LoginForm
        
    return render(request, 'core/login.html', {
            'form': form,
        })

def logout_view(request):
    logout(request)
    return redirect('/')
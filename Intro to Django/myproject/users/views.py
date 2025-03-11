from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('portfolio')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password = password)

            if user:
                login(request, user)
                return redirect('portfolio')
            messages.error(request, f'invalid username or password')
            return render(request, 'user/login.html',{'forms': form})

def sign_out(request):
    logout(rquest)
    return redirect('login')

def sign_up(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('portfolio')
        else:
            return render(request, 'users/register.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .models import PortfolioItem
from .forms import CommentForm
from django.contrig.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def portfolio_list(request):
    items = PortfolioItem.objects.all()
    return render(request,'portfolio/portfolio_list.html', {"itmes":items})

def portfolio_detail(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.portfolio_item = portfolio_item
            comment.author = request.user
            comment.save()
            return redirect('portfolio_detail', pk=portfolio_item.pk)
    else:
        form = CommentForm()
    return render(request, 'portfolio/portfilio_details.html', {'portfolio_item':portfolio_item, 'form':form})

    def register(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form .cleaned_data.get('password1')
                user = authenticate(username=username, password = raw_password)
                login(request, user)
                return redirect('portfolio_list')
            else:
                form = UserCreationForm()
            return render(request, 'registration/register.html', {'form':form})

@login_required
def portfolio_like(require,pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk)
    if portfolio_item.likes.filter(id-request.user.id).exists():
        portfolio_item.likes.remove(request.user)
    else:
        portfilio_item.likes.add(request.user)
    HttpResponseRedirect(reverse('portfolio_detail', args=[str(pk)]))
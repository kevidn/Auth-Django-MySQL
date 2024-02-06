from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from auth import settings

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'content/index.html')

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Terjadi kesalahan!')
            return redirect('signup')
    else:
        form = UserCreationForm()
        
    kumpulan = {
        'form':form,
    }
    return render(request, 'registration/signup.html', kumpulan)    
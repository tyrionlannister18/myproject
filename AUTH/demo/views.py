from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Signupform
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
@login_required
def home(r):
    return render(r,'demo/home.html')

@login_required
def about(r):
    return render(r,'demo/about.html')

def logout(r):
    return render(r,'demo/logout.html')

def signup(r):
    form = Signupform()
    if r.method == 'POST':
        form = Signupform(r.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login")

    return render(r,'demo/signup.html',{"form":form})
from ast import If
from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator


class signup(View):

    def get(self, request, *args, **kwargs):
        form_signup=UserCreationForm()
        return render(request, 'signup.html', {'form_signup': form_signup})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
         form_signup = UserCreationForm()
        if form_signup.is_valid():
          form_signup.save()
        return redirect('sigin')
class home(View):
    
    def get(self, request, *args, **kwargs):
       
        return render(request, 'home.html')

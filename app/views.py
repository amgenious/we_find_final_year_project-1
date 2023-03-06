from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User as user
# Create your views here.




def index(request):
    return render(request, 'index.html',{})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email exists already')
                return redirect('register')
            
            else:
                user = User.objects.create(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                if user is not None:
                    user.save()
                    return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request,'registration.html',{})
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html',{})

class PasswordsChangeView(PasswordChangeView):
        form_class = PasswordChangingForm
        success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'password_success.html',{})


def logout(request):
    auth.logout(request)
    return redirect('index')
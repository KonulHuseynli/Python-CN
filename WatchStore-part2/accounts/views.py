#usere web uzerinden httpresponse qaytaririq
from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

# def say_hi(request): #request-funksiyanin ilk arqumenti olur.Django-da istifadəçidən serverə gələn HTTP sorğusunun bütün məlumatlarını ozunde saxlayan bir obyekt
#     return HttpResponse("Hello, world!") #server istifadəçiyə cavab verir

def sign_in(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, f'Welcome, {user.username}')
            return redirect('all_watches')
        else:
            messages.info(request, f'Daxil etdiyiniz melumatlara uygun user tappilmadi')
    
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('all_watches')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            ###BU CUR YANASMA TAM DOGRU SAYILMAZ
            ###SIGNALS ILE YAZ
            # user = User.objects.get(username=form.cleaned_data.get('username'))#username-i formun daxilinde gonderilen usernameye beraber olan user obyektin getirecek
            # Profile.objects.create(user=user)#uygun useri tapandan sonra profilini yaradir
            return redirect('all_watches')
        messages.error(request, form.errors)
        return redirect('register')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'creation_form': form})

#userpassword
@login_required
def profile(request):
    user = request.user
    profile =  Profile.objects.get(user=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil melumatlari ugurla yenilendi')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'accounts/profile.html', {'profile_form': form, 'profile':profile})
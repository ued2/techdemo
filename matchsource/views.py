from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .models import UserSkill
from .forms import UserSkill
from matchsource.match import match, printing
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

def home(request):
    return render(request, 'matchsource/home.html')


def questionnaire(request):
    if request.method == 'POST':
        forms = UserSkill(request.POST)
        if forms.is_valid():
            forms.save()
            name = request.POST['name']
            skills = request.POST.getlist('skill')
            string = ",".join(skills)
            subject = "Matchsource"
            message = 'Hello ' + name + ',' +\
                ' \nThese are your selected skills [' + string + '].'
            receiver = request.POST['email']
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [receiver], fail_silently=False)

            print('Form Saved Thanks')
            print(request.POST)
        else:
            print(forms.errors)
        return redirect('ms-email')

    forms = UserSkill()

    context = {
        'form': forms
    }

    return render(request, 'matchsource/questionnaire.html', context)


def email(request):
    return render(request, 'matchsource/email.html')


def profile_mining(request):
    return render(request, 'matchsource/mining.html')


def create_account(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            print(request.POST)
            Github = request.POST['Github']
            return redirect('ms-login')
            #if Github == True:
            #    return redirect(ms-ca-questionnaire)
            #print(Github)
            #return redirect()
        
    context = {
        'form': form
    }
    return render(request, 'matchsource/create_account.html', context)


def login_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ms-home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return redirect('ms-login')
    context = {
        'form': form
    }
    return render(request, 'matchsource/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('ms-login')

def  matches(request):
    return render(request, 'matchsource/matches.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import UserSkill
from .forms import UserSkill


def home(request):
    print(request.GET)
    print(request.POST)
    return render(request, 'matchsource/home.html')


def form(request):
    if request.method == 'POST':
        forms = UserSkill(request.POST)
        if forms.is_valid():
            forms.save()
            name = request.POST['name']
            skills = request.POST.getlist('skill')
            string = ",".join(skills)
            subject = "Matchsource"
            message = 'Hi ' + name + ' these are your selected skills ' + string
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

    return render(request, 'matchsource/form.html', context)


def email(request):
    return render(request, 'matchsource/email.html', {'user': request.POST})


def mining(request):
    return render(request, 'matchsource/mining.html')

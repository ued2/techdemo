from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserSkill, ApiSpecific
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# creates the form


class UserSkill(forms.ModelForm):
    # name field
    name = forms.Textarea(attrs={'class': 'form-control',
                                 'placeholder': 'name',
                                 })
    # email field
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'email@abc.com',
                                       }))
    # query skill from database
    allskill = ApiSpecific.objects.distinct('general')
    skill = forms.ModelMultipleChoiceField(queryset=allskill, to_field_name='general', required=True,
                                           initial=0,
                                           label='Select your skills',
                                           widget=forms.SelectMultiple(attrs={'class': 'selectpicker',
                                                                              'placeholder': 'email@abc.com',
                                                                              'data-live-search': "true",
                                                                              'data-width': "100%",
                                                                              'multiple size': "25"
                                                                              }))

    class Meta:
        model = UserSkill
        fields = ['name', 'email', 'skill']



class CreateUserForm(UserCreationForm):
  TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
    )

  Github = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label='Do you have a GitHub Account', 
                              initial='', widget=forms.Select(), required=True)

  class Meta:
    model = User 
    fields = ['username', 'email', 'password1', 'password2', 'Github']

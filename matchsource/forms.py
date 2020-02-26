from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserSkill, ApiSpecific , GitHub
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# creates the form


class UserSkill(forms.ModelForm):
    # name field
    name = forms.Textarea(attrs={'class': 'form-control',
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
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
        }
        fields = ['name', 'email', 'skill']



class CreateUserForm(UserCreationForm):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    github = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label='Do you have a GitHub Account',
                               initial='', widget=forms.Select(), required=True)

    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'github']


class GitHubSearch(forms.ModelForm):

    github = forms.Textarea(attrs={'class': "search-container",
                                 })

    class Meta:
        model=GitHub
        widgets = {
            'github': forms.TextInput(attrs={'placeholder': 'Please enter your GitHub username'}),
        }
        fields=['github']


        
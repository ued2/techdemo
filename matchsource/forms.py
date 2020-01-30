from django import forms
from .models import UserSkill, ApiSpecific

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

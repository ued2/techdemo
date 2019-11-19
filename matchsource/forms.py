from django import forms
from .models import UserSkill, ApiSpecific


class UserSkill(forms.ModelForm):
    name = forms.Textarea(attrs={'class': 'form-control',
                                 'placeholder': 'name',
                                 })
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'email@abc.com',
                                       }))
    allskill = ApiSpecific.objects.distinct('specific')
    skill = forms.ModelMultipleChoiceField(queryset=allskill, to_field_name='specific', required=True,
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

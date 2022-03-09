from cProfile import label
import email
from django import forms
from .models import UserRegistration


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"}),
            'hint_question': forms.Select(attrs={'class': 'form-control', 'required': 'True','autocomplete':"off"})
        }
        labels = {
            'name' : 'Name',
            'email' : 'Email',
            'password' : "Password",
            'confirm_password' : 'Confirm Password',
            'hint_question' : 'Choose Hint Question'
        }
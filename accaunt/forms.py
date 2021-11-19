from django import forms
from django.forms import TextInput
from .models import AdvUser


class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'first_name', 'email', 'password', 'password2')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'first_name': TextInput(attrs={'placeholder': 'First name'}),
            'email': TextInput(attrs={'placeholder': 'Email'})
        }

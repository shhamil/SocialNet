from django import forms
from django.forms import TextInput
from .models import AdvUser, Post


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
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'first_name': TextInput(attrs={'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name'}),
            'email': TextInput(attrs={'placeholder': 'Email'})
        }


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = AdvUser
        fields = ('username', 'first_name', 'last_name', 'about_me', 'email', 'avatar')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'first_name': TextInput(attrs={'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name'}),
            'about_me': TextInput(attrs={'placeholder': 'About me'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
        }


class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user_pk = kwargs.pop('pk', None)
        super(PostCreateForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        user = AdvUser.objects.get(pk=self.user_pk)
        post = super().save(commit=False)
        post.author = user
        post.save()
        return post

    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Title'}),
            'text': TextInput(attrs={'placeholder': 'Post body'}),
        }

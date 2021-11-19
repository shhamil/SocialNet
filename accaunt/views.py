from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserRegistration
from .models import AdvUser, Follower


class IndexView(TemplateView):
    template_name = 'accaunt/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['follower'] = Follower.objects.filter(user_to=self.request.user).count()
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'accaunt/sign_in.html'


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = AdvUser
    template_name = 'accaunt/sign_up.html'
    success_message = 'Вы зарегистрированы!'
    form_class = UserRegistration
    success_url = reverse_lazy('accaunt:sign_in')



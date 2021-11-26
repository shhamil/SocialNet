from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserRegistration, UserSettingsForm, PostCreateForm
from .models import AdvUser, Follower, Post
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from utils.decorators import ajax_required
from actions.utils import create_action


class IndexView(ListView):
    model = Post
    template_name = 'accaunt/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user.pk)
        return queryset


class UserLoginView(LoginView):
    template_name = 'accaunt/sign_in.html'


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = AdvUser
    template_name = 'accaunt/sign_up.html'
    success_message = 'Вы зарегистрированы!'
    form_class = UserRegistration
    success_url = reverse_lazy('accaunt:sign_in')


class UserSettingView(SuccessMessageMixin, UpdateView):
    model = AdvUser
    template_name = 'accaunt/user_settings.html'
    success_message = 'Изменения сохранены!'
    form_class = UserSettingsForm
    success_url = reverse_lazy('accaunt:homepage')

    def get_object(self, queryset=None):
        return self.request.user


class ListUserView(ListView):
    model = AdvUser
    template_name = 'accaunt/list_user.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = AdvUser.objects.all().exclude(pk=self.request.user.pk)
        return queryset


class UserProfileView(DetailView):
    model = AdvUser
    slug_field = 'username'
    context_object_name = 'cntxt_user'
    template_name = 'accaunt/user_profile.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        user = AdvUser.objects.get(username=slug)
        data['user_posts'] = Post.objects.filter(author=user)
        return data


class PostCreateView(CreateView, FormView):
    model = Post
    template_name = 'accaunt/post_create_form.html'
    form_class = PostCreateForm
    success_message = 'Пост создан!'
    success_url = reverse_lazy('accaunt:homepage')

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['pk'] = self.request.user.pk
        return kwargs


class PostDeleteView():
    model = Post
    template_name = 'accaunt/post_delete_view.html'
    succes_url = reverse_lazy('accaunt:delete')


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user_to = AdvUser.objects.get(id=user_id)
            if action == 'follow':
                Follower.objects.get_or_create(user_from=request.user, user_to=user_to)
                create_action(request.user, 'подписался на', user_to)
            else:
                Follower.objects.filter(user_from=request.user, user_to=user_to).delete()
                create_action(request.user, 'отписался от', user_to)
            return JsonResponse({'status': 'ok'})
        except AdvUser.DoesNotExist:
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'ok'})



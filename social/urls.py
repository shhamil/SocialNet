from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView
from .models import Post


class PostCreateView(CreateView):
    model = Post()
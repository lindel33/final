# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Post

from .forms import RegistrForm
from comments.forms import CommentForm


class PostListView(ListView):

    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(self.request.POST or None)
        return context


# Функция регистрации
def Registr(request):
    data = {}
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"

            return render(request, 'registration/registr.html', data)
    else:
        form = RegistrForm()
        data['form'] = form
        return render(request, 'registration/registr.html', data)

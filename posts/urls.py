# -*- coding: utf-8 -*-
from django.urls import path, include

from .views import PostListView, PostDetailView, Registr

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<str:post_slug>', PostDetailView.as_view(), name='post'),
    path('registr/', Registr, name='registr'),
]

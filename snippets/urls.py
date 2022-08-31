from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_snippets, name='list_snippets'),
    path('snippets/<int:pk>', views.snippet_detail, name='snippet_detail'),
    path('snippets/new/', views.create_snippet, name='create_snippet'),
    path('snippets/<int:pk>/edit/', views.snippets_edit, name='snippets_edit'),
    path('delete_snippet/<int:pk>', views.delete_snippet, name="delete_snippet"),
    path('user_profile', views.user_profile, name='user_profile')
]

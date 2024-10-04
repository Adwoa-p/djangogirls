from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('downloadfile/', views.downloadfile, name='downloadfile'),
    path('home/', views.home, name='home'),
    path('main/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]
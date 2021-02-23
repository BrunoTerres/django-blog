from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post')
]
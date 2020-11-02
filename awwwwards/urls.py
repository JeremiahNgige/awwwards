from django.urls import path
from .views import PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', views.index, name='awward-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
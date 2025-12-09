from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='home'),
    path('create/', views.create_post, name='create'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('post/<int:pk>/like/', views.like_post, name='like'),
]
from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('', views.tests_list, name='list'),
    path('<int:test_id>/take/', views.take_test, name='take'),
]
# references/urls.py
from django.urls import path
from . import views

app_name = 'references'

urlpatterns = [
    path('', views.reference_search, name='search'), # /references/
    path('save/', views.save_reference, name='save'),
    path('library/', views.user_library, name='library'),
]
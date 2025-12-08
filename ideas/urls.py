from django.urls import path
from . import views

app_name = "ideas"

urlpatterns = [
    path("", views.idea_list, name="list"),
    path("generate/", views.idea_generate, name="generate"),
    path("<int:pk>/", views.idea_detail, name="detail"),
]

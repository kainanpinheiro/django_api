from django.urls import path

from . import views

urlpatterns = [
    path('teste', views.TesteView.as_view())
]

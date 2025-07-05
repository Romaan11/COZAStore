from django.urls import path
from cozastore import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
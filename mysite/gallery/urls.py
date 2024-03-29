from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test_load, name="test_load"),
    path("test2/", views.test_lazy_load, name="test_lazy_load"),
    path("popup/", views.popup, name="popup"),
    path("viewer/", views.viewer, name="viewer"),
    path("navigation-bar/", views.navigation_bar, name="nav bar"),
    path("home/", views.home, name="home"),
    path("", views.index, name="index"),
]
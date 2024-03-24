from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test_load, name="test_load"),
    path("test2/", views.test_lazy_load, name="test_lazy_load"),
    path("popup/", views.popup, name="popup"),
    path("gallery/", views.gallery, name="gallerryyyyy"),
    path("navigation-bar/", views.navigation_bar, name="nav bar"),

    # ex: /polls/
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path("index", views.get_html, name='index'),
    path("people", views.get_people, name='people'),
    path("detail/<str:name>/", views.show_detail, name='detail'),
]

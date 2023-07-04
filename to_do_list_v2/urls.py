from django.urls import path

from to_do_list_v2.views import home

urlpatterns = [
    path('', home, name="home"),
]

from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^list', views.lists, name="list"),
]
from django.urls import path

app_name = 'api'

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]

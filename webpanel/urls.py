from django.urls import path
from . import views
from django.contrib import admin
from django.views import generic

urlpatterns = [
    path('', views.index, name='webpanel-index'),
    path('controlserver/<path:server_path>/<str:control>', views.controlserver, name='controlserver'),
    path('data/', views.get_data, name='get_data'),
]

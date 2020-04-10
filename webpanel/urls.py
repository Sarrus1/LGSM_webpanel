from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='webpanel-index'),
    path('buttons', views.buttons, name='webpanel-index'),
]

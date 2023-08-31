from django.urls import path
from .views import news_index

urlpatterns = [
    path('',news_index,name='index'),
]
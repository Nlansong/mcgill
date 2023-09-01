from django.urls import path
from .views import news_index

app_name = 'news'

urlpatterns = [
    path('',news_index,name='index'),
]
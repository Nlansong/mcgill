from django.shortcuts import render
from news.models import PostModel


# Create your views here.
def home(request):
    posts = PostModel.objects.all()[0:3]
    context = {
        'title':'McGill University',
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

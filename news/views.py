from django.shortcuts import render
from .models import PostModel, Category

# Create your views here.
def news_index(request):
    posts = PostModel.objects.all()[0:3]
    category = Category.objects.all()
    context = {
        'title': 'NewsRoom',
        'posts':posts,
        'category':category
    }
    return render(request, 'news/index.html', context)

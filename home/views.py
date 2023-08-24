from django.shortcuts import render, redirect
from blog.models import Article
from django.urls import reverse


def home(request):
    articles = Article.objects.all()
    # recent_articles = Article.objects.all().order_by('-created', '-updated')[0:3] # be shekl file context_processors tarif shod
    # return render(request, 'home/home.html', {'articles': articles})
    return render(request, 'home/home.html', {'articles': articles, 'name': "codeyad"})


def sidebar(request):
    data = {'name': 'amirhossein'}
    return render(request, 'includes/sidebar.html', context=data)

from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, number):
    article = Article.objects.get(pk=number)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)

def delete(request, number):
    article = Article.objects.get(pk=number)
    article.delete()
    return redirect('articles:index')

def edit(request, number):
    article = Article.objects.get(pk=number)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, number):
    article = Article.objects.get(pk=number)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

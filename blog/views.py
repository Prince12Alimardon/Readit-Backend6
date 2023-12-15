from django.shortcuts import render, get_object_or_404

from blog.models import Article, Category, Tag


# Create your views here.

def home_page(request):
    article = Article.objects.all().order_by('-id')
    context = {'articles': article}
    return render(request, 'index.html', context)


def blog_page(request):
    article = Article.objects.all().order_by('-id')
    context = {'articles': article}
    return render(request, 'blog.html', context)


def blog_single(request, pk):
    article = get_object_or_404(Article, pk=object.id)
    category = Category.objects.all()
    tag = Tag.objects.all()
    context = {'articles': article, 'categories': category, 'tags': tag}
    return render(request, 'blog-single.html', context)

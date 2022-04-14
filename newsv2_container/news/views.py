from django.shortcuts import render
from . models import Category,Article,Journalist,Tag
# Create your views here.

def article_list(request, category_slug=None, tag_slug=None):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.all().order_by('-date')


    context = {
        'articles': articles,
        'categories': categories,
        'tags':tags
    }

    return render(request, 'article.html', context)
















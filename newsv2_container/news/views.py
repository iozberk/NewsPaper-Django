from django.shortcuts import render
from . models import Category,Article,Journalist,Tag
# Create your views here.

def article_list(request, category_slug=None, tag_slug=None):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.all().order_by('-date')
    flash_news =  Article.objects.filter(available=True).order_by('-id')[:1]

    context = {
        'articles': articles,
        'categories': categories,
        'tags':tags,
        'flash_news' : flash_news,
    }

    return render(request, 'article.html', context)





    










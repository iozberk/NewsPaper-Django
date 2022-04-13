from django.contrib import admin
from . models import Article,Journalist


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'available')
    search_fields = ('title', 'content')

@admin.register(Journalist)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
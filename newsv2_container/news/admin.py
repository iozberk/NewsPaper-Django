from django.contrib import admin
from . models import Article,Journalist,Tag, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'available')
    search_fields = ('title', 'content')

@admin.register(Journalist)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
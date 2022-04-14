from turtle import title
from django.db import models
from PIL import Image


class Journalist(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
        return self.full_name

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"    

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name
        
class Article(models.Model):
    title = models.CharField(max_length=200)
    cre_date = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now = True) # The news must be updated before the news is published.
    content = models.TextField()
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name='journalist')
    available = models.BooleanField(default=True)
    photo = models.ImageField(null=True, blank=True, upload_to = 'newsPhoto/%Y/%m/%d')
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save()
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.photo.path)
    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

















from django.urls import path
from pages.views import IndexView, NewsView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('news/', NewsView.as_view(), name="news"),
]
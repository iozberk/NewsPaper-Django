from django.urls import path
from pages.views import IndexView, NewsView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('article/', NewsView.as_view(), name="articles"),
]
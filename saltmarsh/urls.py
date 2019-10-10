from django.urls import path
from . import views
from .views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<slug>/', ArticleDetailView.as_view(), name="article-detail"),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('about/', views.about, name="about"),
]
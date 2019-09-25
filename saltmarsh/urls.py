from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('about/', views.about, name="about"),
]
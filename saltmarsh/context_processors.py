from .models import Article

def article_count(request):
    return {
        'total_articles': Article.objects.count(),
    }
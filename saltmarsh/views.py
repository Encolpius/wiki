from django.shortcuts import render, redirect, get_object_or_404
from .models import Sessions, Article, Comment
from users.models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import CommentForm
from django.contrib.auth.models import User

recent_comments = Comment.objects.all().order_by("-date_posted")[:5]

def about(request):
    context = {
        'title': 'About',
        'recent_comments': recent_comments,
    }
    return render(request, "saltmarsh/about.html", context)

class ArticleListView(ListView):
    model = Article
    template_name = "saltmarsh/home.html"
    context_object_name = "articles"
    ordering = ['-date_posted']
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['recent_comments'] = recent_comments
        context['pages'] = Article.objects.count()
        return context

class ArticleDetailView(DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        comment_count = Comment.objects.filter(post = post.pk).count()
        context['comment_count'] = comment_count
        context['recent_comments'] = recent_comments
        context['comments'] = Comment.objects.all().order_by("-date_posted")
        return context

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_comments'] = recent_comments
        return context
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article 
    fields = ['title', 'content']
    template_name = "saltmarsh/article_update.html"
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False
    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context['recent_comments'] = recent_comments
        return context

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article 
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False
    def get_context_data(self, **kwargs):
        context = super(ArticleDeleteView, self).get_context_data(**kwargs)
        context['recent_comments'] = recent_comments
        return context

def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = article 
            comment.save()
            return redirect('article-detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'saltmarsh/add_comment_to_article.html', {'form': form})
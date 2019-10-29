from django.shortcuts import render, redirect, get_object_or_404
from .models import Sessions, Article, Comment
from users.models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import CommentForm

def home(request):
    context = {
        'sessions': Sessions.objects.all(),
    }
    return render(request, "saltmarsh/home.html", context)

def about(request):
    return render(request, "saltmarsh/about.html", { 'title': 'About'})

class ArticleListView(ListView):
    model = Article
    template_name = "saltmarsh/home.html"
    context_object_name = "articles"
    ordering = ['-date_posted']
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()[:5]
        return context

class ArticleDetailView(DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post_id=self.object.id).all()
        return context

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article 
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article 
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

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
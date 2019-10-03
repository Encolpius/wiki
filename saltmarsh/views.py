import logging 
log = logging.getLogger(__name__)
from django.shortcuts import render
from .models import Sessions, Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'sessions': Sessions.objects.all()
    }
    return render(request, "saltmarsh/home.html", context)

def about(request):
    return render(request, "saltmarsh/about.html", { 'title': 'About'})

class ArticleListView(ListView):
    model = Article
    template_name = "saltmarsh/home.html"
    context_object_name = "articles"
    ordering = ['-date_posted']

class ArticleDetailView(DetailView):
    model = Article

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
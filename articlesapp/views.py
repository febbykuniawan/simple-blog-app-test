from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from .models import Article
from .forms import ArticleForm

class CreateArticleView(LoginRequiredMixin, CreateView):
    """
    Tampilan untuk membuat artikel baru.
    """

    form_class = ArticleForm
    template_name = 'createArticle.html'
    success_url = reverse_lazy('my-article')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Article created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid form submission.')
        return self.render_to_response(self.get_context_data(form=form))

class MyArticleView(LoginRequiredMixin, ListView):
    """
    Tampilan untuk menampilkan daftar artikel pengguna.
    """

    model = Article
    template_name = 'indexMyArticle.html'
    paginate_by = 10
    success_url = reverse_lazy('my-article')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
    
    def post(self, request, *args, **kwargs):
        article_id = request.POST.get('article_id')
        if article_id:
            article = get_object_or_404(Article, id=article_id)
            if article.author == request.user:
                article.delete()
                messages.success(request, 'Article has been deleted.')
            else:
                messages.error(request, 'You are not allowed to delete this article.')
        else:
            messages.error(request, 'Invalid request.')

        return redirect('my-article')

class EditArticleView(LoginRequiredMixin, UpdateView):
    """
    Tampilan untuk mengedit artikel yang sudah ada.
    """

    model = Article
    form_class = ArticleForm
    template_name = 'editMyArticle.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Article updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid form submission.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('show-article', kwargs={'pk': self.object.pk})

class ShowArticleView(LoginRequiredMixin, DetailView):
    """
    Tampilan untuk menampilkan detail artikel.
    """

    template_name = 'showArticle.html'
    success_url = reverse_lazy('show-article')

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)

        is_author = article.author == request.user

        author_profile = article.author.user_profile
        if request.user in author_profile.followers.all() or is_author:
            context = {'article': article}
            return render(request, self.template_name, context)
        else:
            return redirect('user-profile', username=article.author.username)

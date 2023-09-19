from django.views import generic
from articlesapp.models import Article

class HomeView(generic.ListView):
    """
    Tampilan untuk halaman utama (home).

    Menampilkan daftar artikel dengan membagi halaman setiap 15 artikel.
    """

    model = Article
    template_name = 'home.html'
    paginate_by = 15

    def get_queryset(self):
        return Article.objects.all().order_by('-publication_date')
from django.views.generic import ListView, DetailView

from news.models import News


class AllNewsView(ListView):
    model = News
    template_name = 'all_news.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

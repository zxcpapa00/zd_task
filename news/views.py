from django.views.generic import ListView, DetailView

from news.models import News


class AllNewsView(ListView):
    model = News
    template_name = 'all_news.html'

    def get_queryset(self):
        tag = self.request.GET.get("tag")
        if tag:
            news = self.model.objects.filter(tags__name__in=[tag, ])
            return news
        return super().get_queryset()


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

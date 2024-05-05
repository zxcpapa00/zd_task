from django.views.generic import ListView

from news.models import News


class AllNewsView(ListView):
    model = News
    template_name = 'all_news.html'

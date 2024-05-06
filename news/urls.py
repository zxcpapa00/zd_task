from django.urls import path
from news.views import AllNewsView, NewsDetailView

urlpatterns = [
    path('', AllNewsView.as_view(), name='news'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail')
]

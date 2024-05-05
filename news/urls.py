from django.urls import path
from news.views import AllNewsView

urlpatterns = [
    path('', AllNewsView.as_view(), name='news')
]

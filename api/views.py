from rest_framework.viewsets import ModelViewSet
from api.serializers import NewsSerializer, TagSerializer
from news.models import News, Tag


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TagsViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

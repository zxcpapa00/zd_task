from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import NewsViewSet, TagsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'tags', TagsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

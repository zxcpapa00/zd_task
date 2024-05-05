from django.contrib import admin

from news.models import Tag, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

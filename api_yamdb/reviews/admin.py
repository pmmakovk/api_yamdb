from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'category',
        'genres',
    )
    search_fields = ('genre__name',)
    list_filter = ('year', 'category', 'genre',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('genre')

    def genres(self, obj):
        return " | ".join(map(lambda x: x.name, obj.genre.all()))


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    search_fields = ('name',)
    list_filter = ('name', 'slug',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    search_fields = ('name',)
    list_filter = ('name', 'slug',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'author',
        'score',
        'pub_date',
    )
    search_fields = ('title', 'author',)
    list_filter = ('author', 'score', 'pub_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'review',
        'author',
        'pub_date',
    )
    search_fields = ('review', 'author',)
    list_filter = ('author', 'pub_date',)

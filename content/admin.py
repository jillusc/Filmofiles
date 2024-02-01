from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Film, Review, Comment
from .forms import ReviewForm


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_title', 'genre', 'year', 'director')
    search_fields = ['film_title', 'genre', 'year', 'director']
    list_filter = ('director', 'year', 'genre')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('film_title', 'slug', 'status', 'created_on', 'updated_on')
    search_fields = ['film__film_title']
    list_filter = ('status', 'author')
    ordering = ('-created_on',)
    summernote_fields = ('content',)
    form = ReviewForm
    actions = ['approve_reviews']

    def save_model(self, request, obj, form, change):
        film_title = form.cleaned_data.get('film_title')
        director = form.cleaned_data.get('director')
        year = form.cleaned_data.get('year')
        genre = form.cleaned_data.get('genre')

        film, created = Film.objects.get_or_create(
            film_title=film_title,
            director=director,
            year=year,
            genre=genre
        )

        obj.film = film

        if not obj.pk:
            obj.author = request.user

        super().save_model(request, obj, form, change)

    def film_title(self, obj):
        return obj.film.film_title

    @admin.action(description="Mark selected reviews as approved")
    def approve_reviews(self, request, queryset):
        queryset.update(approved=True, status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'review', 'created_on', 'approved')
    search_fields = ['user_name__username', 'review__film_title']
    list_filter = ('created_on', 'approved')

    @admin.action(description="Approve selected comments")
    def approve_comments(self, request, queryset):
        queryset.update(approved=True, status=1)

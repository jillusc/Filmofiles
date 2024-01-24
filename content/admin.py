from django.contrib import admin
from .models import Film, Review, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_title', 'genre', 'year', 'director')
    search_fields = ['film_title', 'genre', 'year', 'director']
    list_filter = ('director', 'year', 'genre')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('film_title', 'slug', 'status', 'created_on',
                    'updated_on')
    search_fields = ['film_title']
    list_filter = ('status',)
    ordering = ('-created_on',)
    summernote_fields = ('content',)

    def film_title(self, obj):
        return obj.film.film_title


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'review', 'created_on', 'approved')
    search_fields = ['user_name__username', 'review__film_title']
    list_filter = ('created_on', 'approved')

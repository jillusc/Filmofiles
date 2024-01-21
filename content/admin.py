from django.contrib import admin
from .models import Film, Review, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Film)
admin.site.register(Comment)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('film_title', 'slug', 'status', 'created_on',
                    'updated_on')
    search_fields = ['film_title']
    list_filter = ('status',)
    ordering = ('-created_on',)
    summernote_fields = ('content',)

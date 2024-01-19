from django.contrib import admin
from .models import Film, Review, Comment

# Register your models here.
admin.site.register(Film)
admin.site.register(Review)
admin.site.register(Comment)

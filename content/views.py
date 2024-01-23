from django.shortcuts import render
from django.views import generic
from .models import Review, Comment, Film


class ReviewsList(generic.ListView):
    queryset = Review.objects.all().order_by("-created_on")
    template_name = "content/index.html"
    paginate_by = 6

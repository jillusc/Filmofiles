from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review, Comment, Film


class ReviewsList(generic.ListView):
    queryset = Review.objects.all().order_by("-created_on")
    template_name = "content/index.html"
    paginate_by = 6

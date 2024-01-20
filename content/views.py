from django.shortcuts import render
from django.views import generic
from .models import Review, Film

# Create your views here.


class ReviewsList(generic.ListView):
    queryset = Review.objects.all()
    template_name = "content/reviews_list.html"

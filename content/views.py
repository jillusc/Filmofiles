from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Review, Comment, Film
from .forms import ReviewForm, CommentForm


def home(request):
    """ Display the home page with form for submitting a film review. """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
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
            review = form.save(commit=False)
            review.film = film
            review.save()

            return redirect('browse')
    else:
        form = ReviewForm()

    return render(request, "content/index.html", {'form': form})


class ReviewsList(generic.ListView):
    queryset = Review.objects.all().order_by("-created_on")
    template_name = "content/browse.html"
    paginate_by = 6


@login_required
def review_detail(request, slug):
    """ Display an individual film review and associated comments. """
    review = get_object_or_404(Review, slug=slug)
    comments = review.comments.all().order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user_name = request.user
            comment.review = review
            comment.save()
            messages.success(request, 'Comment submitted.')
            return redirect('review_detail', slug=review.slug)

    else:
        comment_form = CommentForm()

    return render(
        request,
        "content/review_detail.html",
        {
            "review": review,
            "comments": comments,
        }
    )

from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Review, Comment, Film
from .forms import ReviewForm, CommentForm


def home(request):
    """
    This renders the home page.
    """
    return render(request, "content/index.html")


def submit_review(request):
    """
    This handles the submission of a film review. It processes and validates
    the form data that is submitted, creates a new Film object if necessary,
    associates the review with the film, and displays appropriate messages.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            film_title = form.cleaned_data.get('film_title')
            director = form.cleaned_data.get('director')
            year = form.cleaned_data.get('year')
            genre = form.cleaned_data.get('genre')
            image = request.FILES.get('image')
            result = cloudinary.uploader.upload(image)
            film, created = Film.objects.get_or_create(
                film_title=film_title,
                director=director,
                year=year,
                genre=genre
            )
            review = form.save(commit=False)
            review.film = film
            review.author = request.user
            review.approved = False
            review.save()
            messages.success(
                request, "Your review is pending approval. Thank you!")

            return redirect('browse', page=1)
        else:
            messages.error(
                request, "There was an error with your submission. "
                         "Please check your information.")
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ReviewForm()

    return render(request, "content/submit_review.html", {'form': form})


class ReviewsList(generic.ListView):
    """
    This displays a list of approved reviews on the Browse page.
    """
    model = Review
    queryset = Review.objects.filter(approved=True).order_by("-created_on")
    template_name = "content/browse.html"
    paginate_by = 6


def review_detail(request, slug):
    """
    This displays the full review on its own page, review_detail.
    """
    review = get_object_or_404(Review, slug=slug)
    comments = review.comments.filter(approved=True).order_by("-created_on")
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST, user=request.user)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
            return redirect('review_detail', slug=slug)
    else:
        comment_form = CommentForm()
    return render(
        request,
        "content/review_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_form": comment_form,
        }
    )


@login_required
def submit_comment(request, review_id):
    """
    This handles the submission of a comment. It validates the form data,
    creates a new comment and associates it with the review; sets the comment's
    author attribute from the logged-in user and marks the comment as
    unapproved. It redirects to the review_detail page with success or error
    messages.
    """
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.approved = False
            comment.save()

            messages.success(request, "Your comment has been submitted.")
            return redirect('review_detail', slug=review.slug)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    return redirect('review_detail', slug=review.slug)

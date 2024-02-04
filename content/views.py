from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
            review = form.save(commit=False)
            review.author = request.user
            review.approved = False
            review.save()
            messages.success(request, "Your review is pending approval. Thank you!")
            return redirect('browse', page=1)
    else:
        form = ReviewForm()

    return render(request, "content/submit_review.html", {'form': form})



def review_detail(request, slug):
    """
    Displays the full review on its own page along with approved comments.
    """
    review = get_object_or_404(Review, slug=slug)
    comments = review.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()
    comment_form = CommentForm()

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been submitted for review.")
            return redirect('review_detail', slug=slug)
    else:
        comment_count = comments.count()
        comment_form = CommentForm()
    return render(
        request,
        "content/review_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_form": comment_form,
            "comment_count": comment_count
        }
    )


class ReviewsList(generic.ListView):
    """
    This displays a list of approved reviews on the Browse page.
    """
    model = Review
    queryset = Review.objects.filter(approved=True).order_by("-created_on")
    template_name = "content/browse.html"
    paginate_by = 6


@login_required
def submit_comment(request, review_id):
    """
    Handles the submission of a comment. It validates the form data,
    creates a new comment and associates it with the review; sets the comment's
    author attribute from the logged-in user and marks the comment as
    unapproved. It redirects to the review_detail page with success or error
    messages.
    """
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.approved = False
            comment.save()
            messages.success(request, "Your comment is pending approval. Thank you!")
            return redirect('review_detail', slug=review.slug)
        else:
            print(form.errors)
            messages.error(request, "There was a problem with your comment submission.")
    else:
        messages.error(request, "Invalid request.")
    return redirect('review_detail', slug=review.slug)



def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

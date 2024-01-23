from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review, Comment, Film


def home(request):
    """ Display the home page. """
    return render(request, "content/index.html")


class ReviewsList(generic.ListView):
    queryset = Review.objects.all().order_by("-created_on")
    template_name = "content/browse.html"
    paginate_by = 6


def review_detail(request, slug):
    """ Display an individual film review and associated comments. """
    review = get_object_or_404(Review, slug=slug)
    comments = review.comments.all().order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
            messages.success(request, 'Comment submitted.')

    comment_form = CommentForm()

    return render(
        request,
        "content/review_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

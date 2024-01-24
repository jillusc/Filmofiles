from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Review, Comment, Film
from .forms import ReviewForm, CommentForm


def home(request):
    """ Display the home page with form for submitting a film review. """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, "content/index.html", {'form': form})


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
        comment_form = CommentForm(request.POST, user=request.user)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            film_title = comment_form.cleaned_data['film_title']
            genre = comment_form.cleaned_data['genre']
            year = comment_form.cleaned_data['year']
            director = comment_form.cleaned_data['director']

            existing_film = Film.objects.filter(
                film_title=film_title,
                genre=genre,
                year=year,
                director=director
            ).first()

            if existing_film:
                comment.film = existing_film
            else:
                new_film = Film.objects.create(
                    film_title=film_title,
                    genre=genre,
                    year=year,
                    director=director
                )
                comment.film = new_film

            comment.user_name = request.user
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


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            film_title = form.cleaned_data.get('film_title')
            genre = form.cleaned_data.get('genre')
            year = form.cleaned_data.get('year')
            director = form.cleaned_data.get('director')

            existing_film = Film.objects.filter(
                film_title=film_title,
                director=director, year=year).first()

            if existing_film:
                film = existing_film
            else:
                film = Film.objects.create(
                    film_title=film_title,
                    director=director,
                    year=year,
                    genre=genre,
                )

            review = form.save(commit=False)
            review.film = film
            review.save()
            request.session['review_submitted'] = True
            return redirect('browse')
    else:
        return redirect('success_page')

import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Review, Film, Comment

current_year = datetime.date.today().year


class ReviewForm(forms.ModelForm):
    film_title = forms.CharField(max_length=100)
    director = forms.CharField(max_length=100)
    year = forms.IntegerField(min_value=1888, max_value=current_year)
    genre = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Share your thoughts on this film'}))
    slug = forms.CharField(max_length=50, required=False)
    rating = forms.IntegerField(
        min_value=0, max_value=10, required=True, label='Rating /10')

    class Meta:
        model = Review
        fields = ['film_title', 'director', 'year',
                  'genre', 'content', 'slug', 'rating']

    def save(self, commit=True):
        review = super().save(commit=False)

        film_title = self.cleaned_data.get('film_title')
        director = self.cleaned_data.get('director')
        year = self.cleaned_data.get('year')
        genre = self.cleaned_data.get('genre')

        film, created = Film.objects.get_or_create(
            film_title=film_title,
            director=director,
            year=year,
            genre=genre
        )

        review.film = film

        if commit:
            review.save()
        return review


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        if self.user:
            comment.user_name = self.user
        if commit:
            comment.save()
        return comment

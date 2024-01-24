import datetime
from django import forms
from .models import Review, Comment

current_year = datetime.date.today().year


class ReviewForm(forms.ModelForm):
    film_title = forms.CharField(
        max_length=150,
        required=False)
    director = forms.CharField(
        max_length=100,
        required=False)
    year = forms.IntegerField(
        min_value=1888,
        max_value=current_year,
        required=False)
    genre = forms.CharField(
        max_length=50,
        required=False)
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Share your thoughts on this film'}))
    slug = forms.CharField(
        max_length=50,
        required=False)

    def clean_slug(self):
        slug = self.cleaned_data['slug']

        if Review.objects.filter(slug=slug).exists():
            raise ValidationError("This tagline already exists! "
                                  "Please modify.")

        return slug

    class Meta:
        model = Review
        fields = ['film_title', 'director', 'year',
                  'genre', 'content', 'slug', 'rating']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if user:
            self.user = user

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.user_name = self.user
        if commit:
            comment.save()
        return comment

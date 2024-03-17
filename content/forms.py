"""
Custom Forms for Review and Comment Models.
"""
import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.text import slugify
from .models import Review, Film, Comment

current_year = datetime.date.today().year


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['slug'] = forms.CharField(required=True, label="Tagline")

    class Meta:
        model = Review
        fields = ['film', 'slug', 'content', 'rating']

    def clean_slug(self):
        slug = self.cleaned_data.get('slug', '')
        new_slug = slugify(slug)
        if new_slug and Review.objects.filter(slug=new_slug).exists():
            raise forms.ValidationError(
                "This tagline already exists. Please write something "
                "different.")
        return new_slug


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': "Share your thoughts "
                                     "on this review..."}))

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

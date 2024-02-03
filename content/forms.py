"""
Custom Forms for Review and Comment Models.
"""
import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Review, Film, Comment

current_year = datetime.date.today().year


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['film', 'slug', 'content', 'rating']

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        new_slug = slug.replace(' ', '-')
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

from django import forms
from .models import Comment


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

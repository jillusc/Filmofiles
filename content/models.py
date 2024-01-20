from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, 'Pending'),
    (1, 'Approved'),
)


class Film(models.Model):
    film_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    director = models.CharField(max_length=100)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    film_title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 11)])
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.film_title} | a review by {self.author}"


class Comment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.user_name} on {self.review.film_title}"
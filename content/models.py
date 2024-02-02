from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True,
                            verbose_name='Tagline')
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 11)],
                                 verbose_name='Rating /10')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.film.film_title} | a review by {self.author}"


class Comment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.user_name} commented on this review:"

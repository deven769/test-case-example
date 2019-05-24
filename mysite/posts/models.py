from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.text


from django.views.generic import ListView
from .models import Post


class PostPageView(ListView):
    model = Post
    template_name = 'posts.html'

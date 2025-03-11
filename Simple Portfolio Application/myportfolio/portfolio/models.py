from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='portfoliopost_like')

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    portfolio_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
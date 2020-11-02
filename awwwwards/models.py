from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title   = models.CharField(max_length=200)
    content = models.TextField()
    image   = models.ImageField(upload_to='post_pics/', blank=True, null=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

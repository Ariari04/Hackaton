from django.db import models
from knox.models import User

RATING_CHOICES = ((1, 1),
                  (2, 2),
                  (3, 3),
                  (4, 4),
                  (5, 5))


class Review(models.Model):
    author = User
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    street = models.CharField(max_length=100, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    description = models.TextField(null=True, blank=True)
    importance = models.BooleanField(default=False)
    longitude = models.FloatField()
    latitude = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created_date',)

    def str(self):
        return '{} by {}'.format(self.title, self.author)

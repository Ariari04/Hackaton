import base64

from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

RATING_CHOICES = ((1, 1),
                  (2, 2),
                  (3, 3),
                  (4, 4),
                  (5, 5))

class Streets(models.Model):
    street_title = models.CharField(max_length=100)
    contractor = models.ForeignKey('Contractors', on_delete=models.CASCADE)
    importance = models.BooleanField(default=False)
    rating = models.FloatField(null=True, blank=True)


class Contractors(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    status = models.PositiveIntegerField(choices=RATING_CHOICES)

    def add_review(self, review):
        if review.street.lower() == self.street_title.lower():
            self.reviews.add(review)



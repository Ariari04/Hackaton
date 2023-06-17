from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, Group, Permission
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import BigAutoField


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

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

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


# import base64
#
# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# from django.core.files.base import ContentFile
# from django.db import models
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
# from django.core.mail import send_mail
#
#
# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
#                                                    reset_password_token.key)
#
#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="Some website title"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@somehost.local",
#         # to:
#         [reset_password_token.user.email]
#     )
#
#
# class User(AbstractUser):
#     phone_number = models.CharField(max_length=20, blank=True)

from django.core.validators import MinLengthValidator
from django.db import models
from account.models import CustomUser
from .validators import number_validator
from .choices import DeliveryChoices


class HelpModel(models.Model):
    question_theme = models.TextField(
        max_length=30,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(5)
        ],
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    question = models.TextField(
        max_length=200,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(5),

        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    current_sender = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='help_requests'
    )

    def __str__(self):
        return f"{self.question_theme} from {self.current_sender}"

class OrderNoProfileModel(models.Model):
    product = models.CharField(
    )

    telephone_number = models.CharField(
        validators=[
            number_validator,
        ]
    )
    price = models.PositiveIntegerField(
    )
    created_at = models.DateTimeField(auto_now_add=True)

class OrderProfileModel(models.Model):
    product = models.CharField(
    )

    telephone_number = models.CharField(
        validators=[
            number_validator,
        ]
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(3),
        ]
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(3),
        ]
    )
    delivery_choices= models.CharField(
        blank=False,
        null=False,
        choices=DeliveryChoices.choices,
    )
    address=models.CharField(
        max_length=100,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(10),
        ]
    )
    logged_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='order_user'
    )
    price = models.PositiveIntegerField(
    )
    created_at = models.DateTimeField(auto_now_add=True)
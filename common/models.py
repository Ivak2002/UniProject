from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from account.models import CustomUser

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

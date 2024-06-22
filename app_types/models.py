from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# from app_users.models import User

# Create your models here.
class Type(models.Model):
    """Types model."""

    NAME_CHOICE = (
        ('Naipes', 'Naipes'),#52
        ('Uno', 'Uno'),#112
        ('Golpe', 'Golpe'),#110
    )

    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, choices=NAME_CHOICE)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='types/photos')

    quantity = models.IntegerField(
        default = 0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
            ]
        )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return name, description, created and modified."""
        return f'{(self.name)} | {(self.created)} | {(self.modified)}'


class Challange(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    types = models.OneToOneField(Type, on_delete=models.CASCADE)
    dificult = models.IntegerField(
        validators=[
            MinValueValidator(1),  # Dificultad mínima
            MaxValueValidator(10)  # Dificultad máxima
        ]
    )
    # created = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{(self.name)} | {(self.description)} | {(self.created)} | {(self.modified)}'

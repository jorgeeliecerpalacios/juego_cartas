from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# from app_users.models import User

# Create your models here.
class Types(models.Model):
    """Types model."""

    NAME_CHOICE=(
        ('baraja', 'Naipes'),#52
        ('cartas', 'Uno'),#112
        ('tarjetas', 'Golpe'),#110
    )

    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
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
        """Return title and username."""
        return f'{(self.name)} | {(self.description)} | {(self.created)} | {(self.modified)}'
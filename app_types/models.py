from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# from app_users.models import User

# Create your models here.
class Type(models.Model):
    """Types model."""

    NAME_CHOICE = (
        ('baraja', 'Naipes'),#52
        ('cartas', 'Uno'),#112
        ('tarjetas', 'Golpe'),#110
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
        """Return title and username."""
        return f'{(self.name)} | {(self.description)} | {(self.created)} | {(self.modified)}'

class Challange(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # juego = models.ForeignKey(JuegoDeCartas, on_delete=models.CASCADE)
    dificult = models.IntegerField(
        validators=[
            MinValueValidator(1),  # Dificultad mínima
            MaxValueValidator(10)  # Dificultad máxima
        ]
    )
    # created = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    premio = models.CharField(max_length=100)
    # Otros campos relevantes para el reto

    def __str__(self):
        return f'{self.name} - {self.description}'

from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_personalizados_groups',  # Evita conflicto con auth.User.groups
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_personalizados_permissions',  # Evita conflicto con auth.User.user_permissions
        blank=True
    )

    def __str__(self):
        return self.username
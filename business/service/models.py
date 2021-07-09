from django.db import models
from django.utils.translation import  gettext_lazy as _

# Create your models here.
class  Service(models.Model):
    title = models.CharField(
        _("Titulo"),
        max_length=200
    ) 
    subtitle = models.CharField(
        _("Subtitulo"),
        max_length=200
    )
    content = models.TextField(
        _("Contenido")
    )
    image = models.ImageField(
        _("Imagen"),
        upload_to = "projects"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = _("Servicio")
        verbose_name_plural = _("Servicios")
    
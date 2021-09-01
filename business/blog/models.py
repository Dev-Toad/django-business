from django.db import models
from django.utils.translation import  ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.timezone import  now


class Category(models.Model):
    name = models.CharField(
        _("Nombre"),
        max_length=100,
    )
    created_at = models.DateTimeField(
        _ ("Fecha de creacion"),
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        _ ("Fecha de edicion"),
        auto_now_add=True,
    )
    class Meta:
        verbose_name =_("Categoria")
        verbose_name_plural =_("Catergorias")
        ordering =["-created_at"]

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(
        max_length=200,
    )
    content = models.TextField(
        _("Contenido"),
        blank=True,
    )
    published = models.DateTimeField(
        _("Fecha de publicacion"),
        default= now
    )
    image = models.ImageField(
        _("Imagen"),
        upload_to = "projects",
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name = "Autor",
        on_delete=models.CASCADE
    )
    category = models.ManyToManyField(
        Category,
        verbose_name = "Categoria",
    )
    created_at = models.DateTimeField(
        _ ("Fecha de creacion"),
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        _ ("Fecha de edicion"),
        auto_now_add=True,
    )
    class Meta:
        verbose_name =_("Blog")
        verbose_name_plural = _("Blogs")
    
    def __str__(self):
        return self.title
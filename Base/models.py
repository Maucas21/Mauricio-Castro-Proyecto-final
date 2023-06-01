from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blog(models.Model):
    BlogSeleccion = (
    ('biología','Biología'),
    ('química','Química'),
    ('fisica','Fisica'),
    ('otros','Otros'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = RichTextField(max_length=200)
    categoria = models.CharField(max_length=15, choices=BlogSeleccion, default='biología')
    descripcion = RichTextField(null=True, blank=True)
    FechaPublicacion = models.DateTimeField(auto_now_add=True)
    ImagenPost = models.ImageField(null=True, blank=True, upload_to="media/")

    class Meta:
        ordering = ['usuario', '-FechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey(Blog, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = RichTextField(null=True, blank=True)
    FechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-FechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)

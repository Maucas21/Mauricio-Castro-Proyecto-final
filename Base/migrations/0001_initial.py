# Generated by Django 4.2 on 2023-04-28 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('categoria', models.CharField(choices=[('biología', 'Biología'), ('química', 'Química'), ('fisica', 'Fisica'), ('otros', 'Otros')], default='biología', max_length=15)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('FechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('ImagenPost', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario', '-FechaPublicacion'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('FechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Base.blog')),
            ],
            options={
                'ordering': ['-FechaComentario'],
            },
        ),
    ]

from django import forms
from Base.models import Blog,Comentario



class FormularioNuevoPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('usuario', 'titulo', 'categoria', 'descripcion', 'ImagenPost')

        widgets = {
            'usuario' : forms.Select(attrs={'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'categoria' : forms.Select(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),

        }

class ActualizacionPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('usuario', 'titulo', 'categoria', 'descripcion', 'ImagenPost')

        widgets = {
            'usuario' : forms.Select(attrs={'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'categoria' : forms.Select(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }


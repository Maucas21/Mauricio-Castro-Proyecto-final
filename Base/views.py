from django.shortcuts import render
from Base.models import Blog,Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from Base.forms import FormularioNuevoPost,ActualizacionPost,FormularioComentario
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView


def mi_vista(request):
    
    return render(request, r"Base/index.html")


# CREACION POST

class PostCreacion(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = FormularioNuevoPost
    success_url = reverse_lazy("inicio")
    template_name = 'Base/Post_creacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreacion, self).form_valid(form)

    
# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'Base/comentario.html'
    success_url = reverse_lazy("inicio")

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)
   
    
#CATEGORIAS 

#Biologia

class BiologiaLista(LoginRequiredMixin, ListView):
    context_object_name = 'biologías'
    queryset = Blog.objects.filter(categoria__startswith='biología')
    template_name = 'Base/lista_biologia.html'
    login_url = "/usuarios/login"


class BiologiaDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'biología'
    template_name = 'Base/biologia_detalle.html'


class BiologiaUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = ActualizacionPost
    success_url = reverse_lazy('lista-biologia')
    context_object_name = 'biología'
    template_name = 'Base/biologia_edicion.html'


class BiologiaBorrar(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('lista-biologia')
    context_object_name = 'biología'
    template_name = 'Base/biologia_borrar.html'

    
#Química

class QuimicaLista(LoginRequiredMixin, ListView):
    context_object_name = 'químicas'
    queryset = Blog.objects.filter(categoria__startswith='química')
    template_name = 'Base/lista_quimica.html'
    login_url = "/usuarios/login"


class QuimicaDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'química'
    template_name = 'Base/quimica_detalle.html'


class QuimicaUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = ActualizacionPost
    success_url = reverse_lazy('lista-quimica')
    context_object_name = 'química'
    template_name = 'Base/quimica_edicion.html'


class QuimicaBorrar(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('lista-quimica')
    context_object_name = 'química'
    template_name = 'Base/quimica_borrar.html'


#Fisica

class FisicaLista(LoginRequiredMixin, ListView):
    context_object_name = 'fisicas'
    queryset = Blog.objects.filter(categoria__startswith='fisica')
    template_name = 'Base/lista_fisica.html'
    login_url = "/usuarios/login"


class FisicaDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'fisica'
    template_name = 'Base/fisica_detalle.html'


class FisicaUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = ActualizacionPost
    success_url = reverse_lazy('lista-fisica')
    context_object_name = 'fisica'
    template_name = 'Base/fisica_edicion.html'


class FisicaBorrar(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('lista-fisica')
    context_object_name = 'fisica'
    template_name = 'Base/fisica_borrar.html'
    
    
#Otros

class OtrosLista(LoginRequiredMixin, ListView):
    context_object_name = 'otross'
    queryset = Blog.objects.filter(categoria__startswith='otros')
    template_name = 'Base/lista_otros.html'
    login_url = "/usuarios/login"


class OtrosDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'otros'
    template_name = 'Base/otros_detalle.html'


class OtrosUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = ActualizacionPost
    success_url = reverse_lazy('lista-otros')
    context_object_name = 'otros'
    template_name = 'Base/otros_edicion.html'


class OtrosBorrar(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('lista-otros')
    context_object_name = 'otros'
    template_name = 'Base/otros_borrar.html' 
from django.urls import path
from Base import views

urlpatterns = [   
    path('', views.mi_vista,name="inicio"),
    
    path('Creacion_post/', views.PostCreacion.as_view(), name='nuevo'),
    
    path('Lista-Biologia/', views.BiologiaLista.as_view() , name='lista-biologia'),
    path('Detalle-Biologia/<int:pk>/', views.BiologiaDetalle.as_view(), name='detalle-biologia'),
    path('Borrar-Biologia/<int:pk>/', views.BiologiaBorrar.as_view(), name='eliminar-biologia'),
    path('Editar-Biologia/<int:pk>/', views.BiologiaUpdate.as_view(), name='editar-biologia'),
    path('Detalle-Biologia/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),
    
    path('Lista-Fisica/', views.FisicaLista.as_view() , name='lista-fisica'),
    path('Detalle-Fisica/<int:pk>/', views.FisicaDetalle.as_view(), name='detalle-fisica'),
    path('Borrar-Fisica/<int:pk>/', views.FisicaBorrar.as_view(), name='eliminar-fisica'),
    path('Editar-Fisica/<int:pk>/', views.FisicaUpdate.as_view(), name='editar-fisica'),
    path('Detalle-Fisica/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),
    
    path('Lista-Quimica/', views.QuimicaLista.as_view() , name='lista-quimica'),
    path('Detalle-Quimica/<int:pk>/', views.QuimicaDetalle.as_view(), name='detalle-quimica'),
    path('Borrar-Quimica/<int:pk>/', views.QuimicaBorrar.as_view(), name='eliminar-quimica'),
    path('Editar-Quimica/<int:pk>/', views.QuimicaUpdate.as_view(), name='editar-quimica'),
    path('Detalle-Quimica/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),
    
    path('Lista-Otros/', views.OtrosLista.as_view() , name='lista-otros'),
    path('Detalle-Otros/<int:pk>/', views.OtrosDetalle.as_view(), name='detalle-otros'),
    path('Borrar-Otros/<int:pk>/', views.OtrosBorrar.as_view(), name='eliminar-otros'),
    path('Editar-Otros/<int:pk>/', views.OtrosUpdate.as_view(), name='editar-otros'),
    path('Detalle-Otros/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),
    
    
    
    ]
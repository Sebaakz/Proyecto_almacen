from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('cliente',views.cliente,name='cliente'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('cliente/crear',views.crear,name='crear'),
    path('cliente/editar/(?P<id>[0-9]+)$',views.editar,name='editar'),
    path('cliente/eliminar/(?P<id>[0-9]+)$',views.eliminar,name='eliminar'),  
]
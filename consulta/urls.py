from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.VisualizarConsultasView.as_view(), name='visualizar_consultas'),
    path('detallesconsulta/<int:pk>/', views.DetallesConsultaView.as_view(), name='detalles_consulta'),
    path('crearconsulta/', views.CrearConsultaView.as_view(), name = 'crear_consulta'),
    path('detallesconsulta/<int:pk>/responderconsulta/', views.ResponderConsultaView.as_view(), name= 'responder_consulta'),
    path('<int:pk>/eliminar', views.ConsultaDeleteView.as_view(), name='consulta_delete'),
    path('<int:pk>/editar', views.ConsultaUpdateView.as_view(), name='consulta_update'),

    #crear, modificar, visualizar y eliminar propuestas de consulta
    path('detallesconsulta/<int:pk>/crearpropuestaconsulta/', views.PropuestaConsultaCreateView.as_view(), name ='crear_propuesta'),
    path('visualizarpropuesta/<int:pk>/', views.PropuestaConsultaVisualizarView.as_view(), name= 'visualizar_propuesta'),
    path('visualizarpropuesta/<int:pk>/editar', views.PropuestaConsultaUpdateView.as_view(), name ='editar_propuesta'),
    path('visualizarpropuesta/<int:pk>/eliminar', views.PropuestaConsultaDeleteView.as_view(), name ='eliminar_propuesta'),
]
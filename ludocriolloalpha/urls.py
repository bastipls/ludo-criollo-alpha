from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('ingreso_profe/', views.ingreso_profe, name='ingreso_profe'),
    path('listar_alumnos_profe/', views.listar_alumnos_profe, name='listar_alumnos_profe'),
    path('listar_alumnos_profe/detalle_alumno_profe/<int:pk>/', views.detalle_alumno_profe, name='detalle_alumno_profe'),
    path('listar_alumnos_profe/detalle_alumno_profe/<int:pk>/modificar_profe/', views.modificar_profe, name='modificar_profe'),
    path('listar_alumnos_profe/detalle_alumno_profe/<int:pk>/modificar_profe/eliminar/', views.eliminar_alumno, name='eliminar_alumno'),
    path('logout/',views.logout_view, name="logout"),
]

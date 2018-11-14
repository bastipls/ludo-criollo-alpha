from django import forms
from .models import Alumno

class AlumnoForm (forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('nombres_alumno','apellidos_alumno','edad_alumno','curso_alumno','peso_alumno','talla_alumno','perimetro_cintura_alumno','fuerza_prensil_izquierda_alumno','fuerza_prensil_derecha_alumno',)
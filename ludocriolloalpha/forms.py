from django import forms
from .models import Alumno

class AlumnoForm (forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['apellidos_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['edad_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['curso_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['peso_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['talla_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['perimetro_cintura_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['fuerza_prensil_izquierda_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['fuerza_prensil_derecha_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['imc_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
        self.fields['categoria_imc_alumno'].widget.attrs.update({'required':'True','readonly':'True'})
    # def __init__(self, *args, **kwargs):
    #     super(AlumnoForm, self).__init__(*args, **kwargs)
    #     self.fields['nombres_alumno'].widget.attrs['readonly'] = True 
    #     self.fields['apellidos_alumno'].widget.attrs['readonly'] = True
    #     self.fields['edad_alumno'].widget.attrs['readonly'] = True
    #     self.fields['curso_alumno'].widget.attrs['readonly'] = True
    #     self.fields['peso_alumno'].widget.attrs['readonly'] = True
    #     self.fields['talla_alumno'].widget.attrs['readonly'] = True
    #     self.fields['perimetro_cintura_alumno'].widget.attrs['readonly'] = True
    #     self.fields['curso_alumno'].widget.attrs['readonly'] = True
    #     self.fields['curso_alumno'].widget.attrs['readonly'] = True
    #     self.fields['curso_alumno'].widget.attrs['readonly'] = True
    #     self.fields['curso_alumno'].widget.attrs['readonly'] = True
    class Meta:
        model = Alumno
        fields = ('id_alumno','nombres_alumno','apellidos_alumno','edad_alumno','curso_alumno','peso_alumno','talla_alumno','perimetro_cintura_alumno','fuerza_prensil_izquierda_alumno','fuerza_prensil_derecha_alumno','imc_alumno','categoria_imc_alumno')
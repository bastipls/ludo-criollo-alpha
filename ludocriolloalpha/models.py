from django.db import models


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombres_alumno = models.CharField(max_length=40)
    apellidos_alumno = models.CharField(max_length=40)
    edad_alumno = models.IntegerField(blank=True,null=True)
    curso_alumno = models.CharField(max_length=3)
    peso_alumno = models.IntegerField(blank=True,null=True)
    talla_alumno = models.IntegerField(blank=True,null=True)
    perimetro_cintura_alumno = models.IntegerField(blank=True,null=True)
    fuerza_prensil_izquierda_alumno = models.IntegerField(blank=True,null=True)
    fuerza_prensil_derecha_alumno = models.IntegerField(blank=True,null=True)
    imc_alumno = models.DecimalField(max_digits=4,decimal_places=2)
    categoria_imc_alumno = models.CharField(max_length=40)

    def __str__(self):
        return self.nombres_alumno


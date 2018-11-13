# Generated by Django 2.1.3 on 2018-11-13 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_alumno', models.CharField(max_length=40)),
                ('apellidos_alumno', models.CharField(max_length=40)),
                ('edad_alumno', models.IntegerField(blank=True, null=True)),
                ('peso_alumno', models.IntegerField(blank=True, null=True)),
                ('talla_alumno', models.IntegerField(blank=True, null=True)),
                ('perimetro_cintura_alumno', models.IntegerField(blank=True, null=True)),
                ('fuerza_prensil_izquierda_alumno', models.IntegerField(blank=True, null=True)),
                ('fuerza_prensil_derecha_alumno', models.IntegerField(blank=True, null=True)),
                ('imc_alumno', models.DecimalField(decimal_places=2, max_digits=4)),
                ('categoria_imc_alumno', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todos_curso', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso_alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ludocriolloalpha.Curso'),
        ),
    ]
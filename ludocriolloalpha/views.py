from django.shortcuts import render,get_object_or_404
from .models import Alumno
from .forms import AlumnoForm
def inicio(request):
              
    return render(request, 'ludocriolloalpha/inicio.html', {})

def ingreso_profe(request):
    todos_cursos = Alumno.objects.values('curso_alumno')
    if request.method == 'POST':
   
        nombresAlumno = request.POST.get('txtname',True)
        apellidosAlumno = request.POST.get('txtlastname',True)
        edadAlumno = request.POST.get('txtage',True)
        cursoAlumno = request.POST.get('txtselectgrade',True)
        pesoAlumno = request.POST.get('txtweight',True)
        tallaAlumno = request.POST.get('txttalla',True)
        perimetroAlumno = request.POST.get('txtperimeter',True)
        fuerzaprensilderechaAlumno = request.POST.get('txtfpizquierda',True)
        fuerzaprensilizquierdaAlumno = request.POST.get('txtfpderecha',True)
        imcAlumno = float(pesoAlumno) / (float(tallaAlumno)/100)**2
        if( imcAlumno < 16):
            categoriaimcAlumno = "Delgadez severa"
        elif( imcAlumno < 16.99):
            categoriaimcAlumno = "Delgadez moderada"
        elif( imcAlumno < 18.49):
            categoriaimcAlumno = "Delgadez aceptable"
        elif( imcAlumno < 24.99):
            categoriaimcAlumno = "Peso normal"
        elif( imcAlumno < 29.99):
            categoriaimcAlumno = "Sobrepeso"
        elif( imcAlumno < 34.99 ):
            categoriaimcAlumno = "Obesidad" 
        else:
            categoriaimcAlumno = "Obesidad morvida"

        atributos = Alumno(nombres_alumno = nombresAlumno,
                           apellidos_alumno = apellidosAlumno,
                           edad_alumno = edadAlumno,
                           curso_alumno = cursoAlumno,
                           peso_alumno = pesoAlumno,
                           talla_alumno = tallaAlumno,
                           perimetro_cintura_alumno = perimetroAlumno,
                           fuerza_prensil_izquierda_alumno = fuerzaprensilizquierdaAlumno,
                           fuerza_prensil_derecha_alumno = fuerzaprensilderechaAlumno,
                           imc_alumno = imcAlumno,
                           categoria_imc_alumno = categoriaimcAlumno)
    
        atributos.save()     
    context = {'todos_cursos':todos_cursos}    
    return render(request,'ludocriolloalpha/ingreso_profe.html',context )

def listar_alumnos_profe(request):
    todos_alumnos = Alumno.objects.all()
    context = {'todos_alumnos':todos_alumnos}
    return  render(request,'ludocriolloalpha/listar_alumnos_profe.html',context)
def detalle_alumno_profe(request,pk):
    alumno = get_object_or_404(Alumno, pk = pk)
    context = {'alumno':alumno}
    return render (request,'ludocriolloalpha/detalle_alumno_profe.html',context)

def modificar_profe(request,pk):
    todos_cursos = Alumno.objects.values('curso_alumno')    
    alumno = get_object_or_404(Alumno,pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST,instance=Alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
    else:
        form = AlumnoForm(instance = alumno)
    context = {'form':form,
               'todos_cursos':todos_cursos}            
    return render(request, 'ludocriolloalpha/modificar_profe.html',context)
        
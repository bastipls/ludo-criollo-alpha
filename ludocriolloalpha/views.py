from django.shortcuts import render,get_object_or_404
from .models import Alumno
from .forms import AlumnoForm
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login ,logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def login_view(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST['txtuser']
        password = request.POST['txtpass']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('ingreso_profe'))
        else:    
            context["error"] = "Credenciales Incorrectas"
            return render(request, 'ludocriolloalpha/login.html', context)
    else:
        return render(request, 'ludocriolloalpha/login.html',context)


    

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

def ingreso_profe(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:    
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
                categoriaimcAlumno = "Obesidad mórbida"

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
    if not request.user.is_authenticated:
        return redirect('login')
    else: 
        todos_alumnos = Alumno.objects.all()



        query = request.GET.get('q')
        if query:
            todos_alumnos = todos_alumnos.filter(
                                                Q(nombres_alumno__icontains=query) |
                                                Q(curso_alumno__icontains=query)
                                                ) 
        context = {'todos_alumnos':todos_alumnos}


        return  render(request,'ludocriolloalpha/listar_alumnos_profe.html',context)



def detalle_alumno_profe(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else: 
        alumno = get_object_or_404(Alumno, pk = pk)
        context = {'alumno':alumno}
        return render (request,'ludocriolloalpha/detalle_alumno_profe.html',context)

def modificar_profe(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else: 
        todos_cursos = Alumno.objects.values('curso_alumno')    
        alumno = get_object_or_404(Alumno,pk=pk)
    
        if request.method == 'POST':
            form = AlumnoForm(request.POST,instance=alumno)
            if form.is_valid():
                pesoAlumno = alumno.peso_alumno
                tallaAlumno = alumno.talla_alumno
                alumno.imc_alumno = float(pesoAlumno) / (float(tallaAlumno)/100)**2
                if( alumno.imc_alumno < 16):
                    alumno.categoria_imc_alumno = "Delgadez severa"
                elif( alumno.imc_alumno < 16.99):
                    alumno.categoria_imc_alumno = "Delgadez moderada"
                elif( alumno.imc_alumno < 18.49):
                    alumno.categoria_imc_alumno = "Delgadez aceptable"
                elif( alumno.imc_alumno < 24.99):
                    alumno.categoria_imc_alumno = "Peso normal"
                elif( alumno.imc_alumno < 29.99):
                    alumno.categoria_imc_alumno = "Sobrepeso"
                elif( alumno.imc_alumno < 34.99 ):
                    alumno.categoria_imc_alumno = "Obesidad" 
                else:
                    alumno.categoria_imc_alumno = "Obesidad mórbida"             
                            
                alumno = form.save(commit=False)
            
                alumno.save()
                return redirect('detalle_alumno_profe',pk=alumno.pk)
        else:
            form = AlumnoForm(instance = alumno)
        context = {'form':form,
                'todos_cursos':todos_cursos,
                'alumno':alumno
                }            
        return render(request, 'ludocriolloalpha/modificar_profe.html',context)

def eliminar_alumno(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else: 
        alumno = get_object_or_404(Alumno,pk=pk)
        alumno.delete()
        
        return redirect('listar_alumnos_profe')
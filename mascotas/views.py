from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import MascotaForm, Mascota, RegistroUsuario
from .models import Mascota

from django.contrib.auth.forms import UserCreationForm

# Esta es la pagina principal de la pagina
def index(request):
    return render(request, 'index.html')


# Vista para hacer login
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error': 'Usuario o contrasenia incorrecta'})
    return render(request, 'login.html')



# Consulta a las mascotas que se crearon sin estar logeado
def consultar_mascotas(request):#uuid
    #mascota = get_object_or_404(Mascota,id_unico= uuid) 
    return render(request, 'consultar_mascotas.html')#,{'mascota': mascota}*/)


@login_required
def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.usuario = request.user  # Asigna el usuario actual
            mascota.save()  # Guarda el modelo ya con el usuario asignado
            return redirect('lista_mascotas')  # Redirige a la lista
    else:
        form = MascotaForm()

    return render(request, 'registrar_mascota.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar_usuario.html', {'form': form})

@login_required
def lista_mascotas(request):
    mascotas = Mascota.objects.filter(usuario=request.user)  # Solo las del usuario
    return render(request, 'lista.html', {'mascotas': mascotas})

# Pruebas de render
def registro(request): # Recibe el request desde el navegador
    if request.method == 'POST': # Verifica que el request sea un metodo POST
        form = RegistroUsuario(request.POST) # Si el metodo es valido envia el metodo POST a la clase que esta almacenada en forms.py donde hace las validaciones de los campos
        if form.is_valid(): # Verifica que el objeto form creado sea valido
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data ['email']
            
            return render(request, 'registro_exitoso.html',{'nombre':nombre, 'email': email})
    else:
        form = RegistroUsuario()
    return render(request, 'registro.html',{'form':form})

def registro_exitoso(request):
    return render(request,'registro_exitoso.html')

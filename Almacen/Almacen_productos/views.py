from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
def inicio(request):
    return render(request,'paginas/inicio.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/index')
    else:
        if request.method == 'POST':
            campo_username = request.POST.get('campo_username')
            Campo_password = request.POST.get('Campo_password')

            user = authenticate(request, username = campo_username, password=Campo_password)

            if user is not None:
                login(request,user)
                return redirect('cliente')
            else:
                messages.info(request,'Usuario o password incorrecto')
        return render(request,'paginas/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def cliente(request):
    clientes= Cliente.objects.all()
    print(clientes)
    return render(request,'clientes/index.html',{'clientes': clientes})
def crear(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cliente')
    return render(request,'clientes/crear.html', {'formulario': formulario})
def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cliente')
    return render(request,'clientes/editar.html', {'formulario': formulario})
def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('cliente')
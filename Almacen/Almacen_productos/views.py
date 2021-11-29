from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ClienteForm
# Create your views here.
def inicio(request):
    return render(request,'paginas/inicio.html')


def cliente(request):
    clientes= Cliente.objects.all()
    print(clientes)
    return render(request,'clientes/index.html',{'clientes': clientes})
def nosotros(request):
    return render(request,'paginas/nosotros.html')
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
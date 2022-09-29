from multiprocessing import context
from django.shortcuts import redirect, render
from usuarios.forms import UsuarioForm

from usuarios.models import Usuario

# Create your views here.


def usuarios(request):

    usuarios= Usuario.objects.all()

    context={
        "usuarios":usuarios
    }
    return render(request,'usuarios/usuarios.html',context)

def usuarios_crear(request):

    if request.method == 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            print("El usuario se guardo correctamente")
            return redirect('usuarios')
        else:
            print("El usuario no se guardo")
    else:
        form= UsuarioForm()
    context={
        "form":form
    }
    return render(request,'usuarios/usuarios-crear.html',context)

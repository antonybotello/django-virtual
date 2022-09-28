from django.shortcuts import render


def holamundo(request):
   titulo = "Inicio"
   nombre = "Antony Botello"

   context = {
      'nombres': nombre,
      'titulo': titulo
   }

   return render(request, 'index.html', context)


def precios(request):
   titulo = "Precios"
   context = {
      'titulo': titulo
   }

   return render(request, 'precios.html', context)

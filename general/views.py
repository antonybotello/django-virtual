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
   lista=["1000 users included!","2 GB of storage","Email support","Help center access"]

   titulo = "Precios"
   context = {
      'titulo': titulo,
      'lista':lista
   }

   return render(request, 'precios.html', context)

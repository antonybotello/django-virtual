from django.shortcuts import render

def holamundo(request):
    nombre="Antony Botello"
    
    context={
       'nombres':nombre 
    }

    return render(request,'index.html',context)
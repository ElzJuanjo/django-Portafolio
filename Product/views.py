from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def detalles(request, idProducto):
    try:
        proyecto = Producto.objects.get(ID=idProducto)
    except:
        return redirect('/productos/')
    
    userLogged = request.session.get('userLogged', False)
    userName = request.session.get('userName', "")
    return render(request, 'detalles.html', {
        "userLogged": userLogged,
        "userName":userName,
        "nombre": proyecto.NOMBRE,
        "categoria": proyecto.CATEGORIA,
        "cliente": proyecto.CLIENTE,
        "fecha": proyecto.FECHA,
        "url": proyecto.URL,
        "desc": proyecto.DESCRIPCION
    })
    
def productos(request):
    userLogged = request.session.get('userLogged', False)
    userName = request.session.get('userName', "")
    return render(request, 'productos.html',{
        "userLogged": userLogged,
        "userName":userName
    })

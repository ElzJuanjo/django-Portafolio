from django.shortcuts import render,redirect
from .models import Usuario, Persona

# Create your views here.
def inicio(request):
    userLogged = request.session.get('userLogged', False)
    userName = request.session.get('userName', "")
    return render(request, 'inicio.html',{
        "userLogged": userLogged,
        "userName":userName
    })

def registro(request): 
    userLogged = request.session.get('userLogged', False)
    if userLogged:
        return redirect('/')
    else:
        error = ""
        if request.method == 'POST':
            user = request.POST['user']
            usuarioExistente = Usuario.objects.filter(USUARIO=user)
            if not usuarioExistente:
                password = request.POST['password']
                password2 = request.POST['password2']
                if password != password2:
                    error = "Las contraseñas ingresadas no coinciden."
                else:
                    nuevoUsuario = Usuario.objects.create(USUARIO=user, CLAVE=password)
                    name = request.POST['name']
                    lastname = request.POST['lastname']
                    email = request.POST['email']
                    born = request.POST['born']
                    nuevaPersona = Persona.objects.create(NOMBRE=name,APELLIDO=lastname,EMAIL=email,FECHA_NACIMIENTO=born)
                    
                    request.session['userName'] = user
                    request.session['userLogged'] = True

                    return redirect('/')
            else:
                error = f"El nombre de usuario {user} ya se encuentra en uso."
                
        request.session['userLogged'] = False
        request.session['userName'] = ""
        return render(request, 'registro.html',{
            "error":error
        })

def login(request):
    userLogged = request.session.get('userLogged', False)
    if userLogged:
        return redirect('/')
    else:
        error = ""
        if request.method == 'POST':
            try:
                registro = Usuario.objects.get(USUARIO=request.POST['user'])
                if registro.CLAVE == request.POST['password']:
                    request.session['userName'] = request.POST['user']
                    request.session['userLogged'] = True
                    return redirect('/')   
                else:
                    error = "La contraseña ingresada es incorrecta."                 
            except:
                error = "Este nombre de usuario no se encuentra registrado."
                
        return render(request, 'login.html',{
            "error":error
        })
        
def perfil(request):
    userLogged = request.session.get('userLogged', False)
    if userLogged:
        error = ""
        datosUsuario = Usuario.objects.get(USUARIO=request.session.get('userName', ""))
        datosPersona = Persona.objects.get(ID_USUARIO=datosUsuario.ID)
        if request.method == 'POST':
            if datosUsuario.CLAVE == request.POST['password']:
                if request.POST['newname'].strip():
                    datosPersona.NOMBRE = request.POST['newname']
                
                if request.POST['newlastname'].strip():     
                    datosPersona.APELLIDO = request.POST['newlastname']
                    
                if request.POST['newemail'].strip():
                    datosPersona.EMAIL = request.POST['newemail']
                    
                if request.POST['newuser'].strip():
                    datosUsuario.USUARIO = request.POST['newuser']
                  
                if  request.POST['password2'].strip():
                    datosUsuario.CLAVE = request.POST['password2']
                    
            else:
                error="La contraseña actual ingresada no es correcta."     
        
        datosUsuario.save()
        datosPersona.save()
        
        return render(request, 'perfil.html',{
            "nombre":datosPersona.NOMBRE,
            "apellido":datosPersona.APELLIDO,
            "email":datosPersona.EMAIL,
            "user":datosUsuario.USUARIO,
            "error":error
        })
        
    else:
        return redirect('/')
    
def cerrarSesion(request):
    userLogged = request.session.get('userLogged', False)
    if userLogged:
        request.session['userLogged'] = False
        request.session['userName'] = "" 
    return redirect('/')

def eliminarCuenta(request):
    userLogged = request.session.get('userLogged', False)
    if userLogged:
        datosUsuario = Usuario.objects.get(USUARIO=request.session.get('userName', ""))
        datosUsuario.delete()
        request.session['userLogged'] = False
        request.session['userName'] = "" 
    return redirect('/')
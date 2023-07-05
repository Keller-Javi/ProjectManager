from django.shortcuts import render, redirect, get_object_or_404
from PM_APP.models import Project, Task
from PM_APP.forms import ProjectForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        print('1')
        if request.POST['password1'] == request.POST['password2']:
            print('2')
            try:
                print('2.a')
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user) # Guarda la sesión usando las cookies 
                return redirect('home')
            except: # puede dar un error si el usuario ya está en la DB
                print('2.b')
                return render(request, 'signup.html', {'error': 'El nombre de usuario ya existe.'})
        else:
            print('3')
            return render(request, 'signup.html', {'error': 'Las contraseñas no coinciden.'})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # verifica el nombre de usuario y la contraseña y obtiene al usuario

        if user is None: # si no guardo nada, es que no se encontro el usuario
            return render(request, 'signin.html', {'error': 'La contraseña o el usuario es incorrecto'})
        else:
            login(request, user)
            return redirect('home')

def logout_(request):
    logout(request)
    return redirect('signin')

def home (request):    
    projects = Project.objects.filter(user=request.user)
    return render(request, 'index.html', {'projects':projects})

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {'form': ProjectForm})
    else:
        try:
            form = ProjectForm(request.POST) # Se obtiene los datos del formulario
            new_project = form.save(commit=False) # con el commit false solo se devuelve los datos del formulario 
            new_project.user = request.user # se enlaza el proyecto al usuario actual
            new_project.save() # se guarda en la tabla de la DB
            return redirect('home')
        except ValueError:
            return render(request, 'create_project.html', {'form': ProjectForm, 'error': 'Ingrese datos validos!.'})

def done_project(request, id):
    project = get_object_or_404(Project, id=id, user=request.user)
    project.date_completed = timezone.now()
    project.save()

    return redirect('home')

def delete_project(request, id):
    project = get_object_or_404(Project, id=id, user=request.user)
    if request.method == 'GET':
        return render(request, 'confirm_elimination.html', {'project': project})
    else:
        project.delete()
        return redirect('home')

def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'GET':
        form = ProjectForm(instance=project) # el instance indica que se  trabajo sobre este proyecto
        return render(request, 'create_project.html', {'form': form, 'project': project})
        # para este caso reutilizo la pagina de crear un proyecto, para no tener que crear otro archivo
    else:
        try:
            form = ProjectForm(request.POST, instance=project)
            project_edit = form.save(commit=False)

            if request.POST['state'] == 'Completado' and not project_edit.date_completed: # se cambia a completado si no se a completado
                project_edit.date_completed = timezone.now()
            elif request.POST['state'] == 'NoCompletado' and project_edit.date_completed: # se cambia a no completado si se a completado
                project_edit.date_completed = None

            project_edit.save()
            return redirect('home')
        except ValueError:
            return render(request, 'create_project.html', {'form': ProjectForm, 'project': project, 'error': 'Ingrese datos validos!.'})
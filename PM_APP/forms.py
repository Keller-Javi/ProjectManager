from django import forms
from PM_APP.models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta: 
        model = Project
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el nombre del proyecto...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba alguna descrición del proyecto...'})
        } 

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el titulo de la tarea...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba alguna descrición de la tarea...'})
        }
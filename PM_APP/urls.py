from django.urls import path
from PM_APP import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("home", views.home, name="home"),  
    path("create_project", views.create_project, name="create_project"),
    path("done_project/<int:id>", views.done_project, name="done_project"),
    path("delete_project/<int:id>", views.delete_project, name="delete_project"),
    path("edit_project/<int:id>", views.edit_project, name="edit_project"),
    path("logout", views.logout_, name="logout"),

    path("tasks/<int:project_id>", views.tasks, name="tasks"),
    path("create_task/<int:project_id>", views.create_task, name="create_task"),
    path("inprocess_task/<int:id>", views.inprocess_task, name="inprocess_task"),
    path("done_task/<int:id>", views.done_task, name="done_task"),
    path("delete_task/<int:id>", views.delete_task, name="delete_task"),
    path("edit_task/<int:id>", views.edit_task, name="edit_task"),
]

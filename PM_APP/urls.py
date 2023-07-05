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
]

from django.urls import path
from projects.views import project_list, show_project, create_project


urlpatterns = [
    path("create/", create_project, name="create_project"),
    path("<int:id>/", show_project, name="show_project"),
    path("", project_list, name="list_projects"),
    path("projects/", project_list),
]

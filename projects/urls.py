from django.urls import path
from projects.views import project_list, show_project


urlpatterns = [
    path("<int:id>/", show_project, name="show_project"),
    path("", project_list, name="list_projects"),
    path("projects/", project_list),
]

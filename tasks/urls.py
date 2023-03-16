from django.urls import path
from tasks.views import create_task, show_my_tasks, update_task


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("update/<int:id>", update_task, name="update_task"),
]

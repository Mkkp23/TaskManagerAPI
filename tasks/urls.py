from django.urls import path

# local imports
from tasks.views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path(
        "tasks/<int:pk>/", TaskRetrieveUpdateDestroyView.as_view(), name="task-detail"
    ),
]

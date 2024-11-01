from django.urls import path

# local imports
from tasks.views import TaskListCreateView, TaskRetrieveUpdateDestroyView

# authentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path(
        "tasks/<int:pk>/", TaskRetrieveUpdateDestroyView.as_view(), name="task-detail"
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from homework_8.views.v2.tasks import (
    TaskListCreateView,
    TaskDetailUpdateDeleteView,
    TaskListByOwnerView
)
from homework_8.views.v2.subtasks import (
    SubtaskListCreateView,
    SubtaskDetailUpdateDeleteView
)
from homework_8.views.v2.categories import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view()),
    path('subtasks/', SubtaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubtaskDetailUpdateDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('my-tasks/', TaskListByOwnerView.as_view())
]

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from homework_8.models import Task, Subtask
from homework_8.views.v2.paginator import AppBasePaginator


class BaseTaskListCreateView(ListCreateAPIView):
    base_model = None
    serializer_get = None
    serializer_post = None

    # NOTE: It's disabled cause the new general pagination was applied for whole project
    # pagination_class = AppBasePaginator
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']   # Поля для фильтрации
    search_fields = ['title', 'description']    # Поля для поиска
    ordering_fields = ['created_at']            # Поля для сортировки

    def get_queryset(self):
        assert self.base_model is not None, (
                "'%s' should include a `base_model` attribute."
                % self.__class__.__name__
        )
        return self.base_model.objects.all()

    def get_serializer_class(self):
        assert self.serializer_get is not None, (
                f"'{self.__class__.__name__}' should include a "
                f"`serializer_get` attribute."
        )
        assert self.serializer_post is not None, (
                f"'{self.__class__.__name__}' should include a "
                f"`serializer_post` attribute."
        )

        if self.request.method == 'GET':
            return self.serializer_get

        else:
            return self.serializer_post


class BaseTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    base_model: Task | Subtask = None
    serializer_get = None
    serializer_put = None

    def get_queryset(self):
        assert self.base_model is not None, (
                f"'{self.__class__.__name__}' should include a `base_model` attribute."
        )
        return self.base_model.objects.all()

    def get_object(self):
        return get_object_or_404(self.base_model, pk=self.kwargs['pk'])

    def get_serializer_class(self):
        assert self.serializer_get is not None, (
                f"'{self.__class__.__name__}' should include a "
                f"`serializer_get` attribute."
        )
        assert self.serializer_put is not None, (
                f"'{self.__class__.__name__}' should include a "
                f"`serializer_put` attribute."
        )

        if self.request.method in ['PUT', 'PATCH']:
            return self.serializer_put
        else:
            return self.serializer_get

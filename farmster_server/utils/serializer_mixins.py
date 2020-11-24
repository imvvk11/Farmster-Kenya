from rest_framework import status
from rest_framework.response import Response


class ReadWriteSerializerMixin:
    def get_serializer_class(self):
        assert self.read_serializer_class is not None, (
                "'%s' should either include a `read_serializer_class` attribute"
                % self.__class__.__name__
        )
        assert self.write_serializer_class is not None, (
                "'%s' should either include a `write_serializer_class` attribute"
                % self.__class__.__name__
        )
        if self.request.method == 'POST' or self.request.method == 'PATCH' or self.request.method == 'PUT':
            return self.write_serializer_class
        return self.read_serializer_class


class CreateModelWithFullResultMixin(ReadWriteSerializerMixin):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        read_serializer = self.read_serializer_class(instance=serializer.instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UpdateModelWithFullResultMixin(ReadWriteSerializerMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        read_serializer = self.read_serializer_class(instance=serializer.instance)
        return Response(read_serializer.data)

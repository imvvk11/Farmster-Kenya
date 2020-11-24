from rest_framework import generics, status
from rest_framework.response import Response

from farmster_server.serializers.crop import CropSerializer
from farmster_server.services import user as user_service


class UserCropsListCreateApi(generics.ListAPIView):
    serializer_class = CropSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = user_service.get_user_crops(user_id)
        return queryset

    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        crop_id = request.data['crop_id']
        user = user_service.add_crop_for_user(crop_id, user_id)
        serializer_class = self.get_serializer_class()
        return Response(data=serializer_class(user.crops, many=True).data, status=status.HTTP_201_CREATED)


class UserCropsDestroy(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        crop_id = kwargs['crop_id']
        user_service.remove_crop_from_user(crop_id, user_id)
        # The valid status is 204, changed to solve client error
        return Response(status=status.HTTP_200_OK)


user_crops_list_create = UserCropsListCreateApi.as_view()
user_crops_destroy = UserCropsDestroy.as_view()

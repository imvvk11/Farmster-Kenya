from rest_framework import generics, status
from rest_framework.response import Response

from farmster_server.serializers.farmer import FarmerFullSerializer
from farmster_server.services import user as user_service


class UserFarmerListCreateApi(generics.ListCreateAPIView):
    serializer_class = FarmerFullSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = user_service.get_user_farmers(user_id)
        return queryset

    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        farmer_id = request.data['farmer_id']
        user = user_service.add_farmer_for_user(farmer_id, user_id)
        serializer_class = self.get_serializer_class()
        return Response(data=serializer_class(user.farmers, many=True).data, status=status.HTTP_201_CREATED)


class UserFarmerDestroyApi(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        farmer_id = kwargs['farmer_id']
        user_service.remove_farmer_from_user(farmer_id, user_id)
        # The valid status is 204, changed to solve client error
        return Response(status=status.HTTP_200_OK)


user_farmer_list_create = UserFarmerListCreateApi.as_view()
user_farmer_destroy = UserFarmerDestroyApi.as_view()

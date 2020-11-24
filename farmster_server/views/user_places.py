from rest_framework import generics, status
from rest_framework.response import Response

from farmster_server.serializers.place import PlaceWithDistanceSerializer, PlaceFullSerializer
from farmster_server.services import user as user_service


class UserPlacesListCreateApi(generics.ListAPIView):
    serializer_class = PlaceWithDistanceSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = user_service.get_user_places(user_id)
        return queryset

    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        place_id = request.data['place_id']
        user = user_service.add_place_for_user(place_id, user_id)
        serializer_class = PlaceFullSerializer
        return Response(data=serializer_class(user.places, many=True).data, status=status.HTTP_201_CREATED)


class UserPlacesDestroy(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        place_id = kwargs['place_id']
        user_service.remove_place_from_user(place_id, user_id)
        # The valid status is 204, changed to solve client error
        return Response(status=status.HTTP_200_OK)


user_places_list_create = UserPlacesListCreateApi.as_view()
user_places_destroy = UserPlacesDestroy.as_view()

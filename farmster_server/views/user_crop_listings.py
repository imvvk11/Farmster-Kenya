from rest_framework import generics, status
from rest_framework.response import Response

from farmster_server.serializers.crop_listing import CropListingFullSerializer
from farmster_server.services import user as user_service


class UserCropListingsListCreateApi(generics.ListAPIView):
    serializer_class = CropListingFullSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = user_service.get_user_crop_listings(user_id)
        return queryset

    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        crop_listing_id = request.data['crop_listing_id']
        user = user_service.add_crop_listing_for_user(crop_listing_id, user_id)
        serializer_class = self.get_serializer_class()
        return Response(data=serializer_class(user.favorite_crop_listings, many=True).data, status=status.HTTP_201_CREATED)


class UserCropListingsDestroy(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        crop_listing_id = kwargs['crop_listing_id']
        user_service.remove_crop_listing_from_user(crop_listing_id, user_id)
        return Response(status=status.HTTP_200_OK)


user_crop_listings_list_create = UserCropListingsListCreateApi.as_view()
user_crop_listings_destroy = UserCropListingsDestroy.as_view()

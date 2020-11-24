from rest_framework.response import Response
from rest_framework import generics, status

from farmster_server.serializers import farmer as farmer_serializer
from farmster_server.serializers import deal as deal_serializer
from farmster_server.serializers import place as place_serializer
from farmster_server.serializers import bot_create as bot_serializer
from farmster_server.services import deal as deal_service
from farmster_server.services import deal_part as deal_part_service
from farmster_server.services import place as place_service
from farmster_server.services import farmer as farmer_service
from farmster_server.services import crop as crop_service


class BotCreatePlaceApi(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer_class = bot_serializer.BotCreatePlaceSerializer(data=self.request.data)
        if serializer_class.is_valid(raise_exception=True):
            place = place_service.get_or_create_place_by_name_district(serializer_class.validated_data)
            return Response(data=place_serializer.PlaceFullSerializer(place).data, status=status.HTTP_201_CREATED)


class BotCreateFarmerApi(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer_class = bot_serializer.BotCreateFarmerSerializer(data=self.request.data)
        if serializer_class.is_valid(raise_exception=True):
            if serializer_class.validated_data['last_name'] is None:
                serializer_class.validated_data['last_name'] = ''

            farmer = farmer_service.get_or_create_farmer_by_phone_number(serializer_class.validated_data)
            return Response(data=farmer_serializer.FarmerFullSerializer(farmer).data, status=status.HTTP_201_CREATED)


class BotCreateDealApi(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer_class = bot_serializer.BotCreateDealsSerializer(data=self.request.data)
        if serializer_class.is_valid(raise_exception=True):
            if serializer_class.validated_data['farmer_last_name'] is None:
                serializer_class.validated_data['farmer_last_name'] = ''

            dict_farmer = {'first_name': serializer_class.validated_data.pop('farmer_first_name'),
                           'last_name': serializer_class.validated_data.pop('farmer_last_name'),
                           'phone_number': serializer_class.validated_data.pop('farmer_phone_number')}

            farmer = farmer_service.get_or_create_farmer_by_phone_number(dict_farmer)
            deal_parts_data = serializer_class.validated_data.pop('deal_parts')
            deal = deal_service.create_deal_from_bot(farmer, serializer_class.validated_data)
            for deal_part in deal_parts_data:
                crop = crop_service.get_crop_by_id(deal_part['crop'])
                deal_part['crop'] = crop
                deal_part_service.create_deal_part(deal, deal_part)
            return Response(data=deal_serializer.DealFullSerializer(deal).data, status=status.HTTP_201_CREATED)


bot_create_place = BotCreatePlaceApi.as_view()
bot_create_farmer = BotCreateFarmerApi.as_view()
bot_create_deal = BotCreateDealApi.as_view()


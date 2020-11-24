from django.db.models import QuerySet

from farmster_server.models.deal import Deal


def get_all_deals() -> QuerySet:
    return Deal.objects.all()


def create_deal(user_id, validated_data):
    return Deal.objects.create(user_id=user_id, **validated_data)


def create_deal_from_bot(farmer, validated_data):
    return Deal.objects.create(farmer=farmer, **validated_data)


def update_deal(instance, validated_data):
    instance.farmer = validated_data.get('farmer', instance.farmer)
    instance.save()


def get_all_crop_listings_by_farmer_id(farmer_id: int) -> QuerySet:
    return Deal.objects.get_all_deals_by_farmer_id(farmer_id)

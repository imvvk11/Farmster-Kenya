from django.db.models import QuerySet

from farmster_server.models.deal_part import DealPart


def create_deal_part(deal, deal_part):
    return DealPart.objects.create(deal=deal, **deal_part)


def update_deal_part(deal_parts, deal_parts_data):
    for deal_part in deal_parts_data:
        deal_parts.crop = deal_part.get(
            'crop',
            deal_parts.crop
        )
        deal_parts.date = deal_part.get(
            'date',
            deal_parts.date
        )
        deal_parts.shipping_method = deal_part.get(
            'shipping_method',
            deal_parts.shipping_method
        )
        deal_parts.price = deal_part.get(
            'price',
            deal_parts.price
        )
        deal_parts.pricing_type = deal_part.get(
            'pricing_type',
            deal_parts.pricing_type
        )
        deal_parts.amount = deal_part.get(
            'amount',
            deal_parts.amount
        )
        deal_parts.amount_unit = deal_part.get(
            'amount_unit',
            deal_parts.amount_unit
        )
        deal_parts.crop_quality = deal_part.get(
            'crop_quality',
            deal_parts.crop_quality
        )
        deal_parts.crop_size = deal_part.get(
            'crop_size',
            deal_parts.crop_size
        )
        deal_parts.save()

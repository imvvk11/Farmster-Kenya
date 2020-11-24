from django.db.models import QuerySet

from farmster_server.models.contact import Contact


def get_all_contacts() -> QuerySet:
    return Contact.objects.all()


def create_contact(user_id, validated_data):
    return Contact.objects.create(user_id=user_id, **validated_data)




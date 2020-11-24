import africastalking

from farmster_server import settings


username = settings.AFRICA_TALKING_USERNAME
api_key = settings.AFRICA_TALKING_API_KEY
africastalking.initialize(username, api_key)


def send_sms(phone_number: str, msg: str):
    sms = africastalking.SMS
    result = sms.send(msg, [phone_number], "Farmster")
    return result

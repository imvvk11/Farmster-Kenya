import boto3

from farmster_server import settings


def send_sms(phone_number: str, msg: str):
    client = boto3.client(
        'sns',
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_ACCESS_SECRET,
        region_name=settings.AWS_REGION
    )

    sender_id = 'Farmster'
    result = client.publish(
        PhoneNumber=phone_number,
        Message=msg,
        MessageAttributes={'AWS.SNS.SMS.SenderID': {'DataType': 'String', 'StringValue': sender_id},
                           'AWS.SNS.SMS.SMSType': {'DataType': 'String', 'StringValue': 'Transactional'}}
    )
    return result

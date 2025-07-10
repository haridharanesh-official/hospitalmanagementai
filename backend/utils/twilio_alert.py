
from twilio.rest import Client

def send_alert_if_needed(data, reasons):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message_body = f"⚠️ ALERT for Patient {data['patient_id']}:\n" + "\n".join(reasons)

    client.messages.create(
        to='+918508511975',
        from_='+15005550006',
        body=message_body
    )

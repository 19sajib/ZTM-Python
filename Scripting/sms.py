from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+8801XXXXXXXXX',
    body='Hello Sajib, this is your bot JARVIS! Good Morning!',
    to='+8801XXXXXXXXX'
    )

print(message.sid)
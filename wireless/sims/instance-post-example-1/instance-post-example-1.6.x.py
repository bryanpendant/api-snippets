# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# required for all twilio access tokens
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

callback_url = 'https://sim-manager.mycompany.com' \
               '/sim-update-callback/AliceSmithSmartMeter'
sim = client.wireless.sims('DEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')\
    .update(
        status='active',
        callback_url=callback_url,
        callback_method='POST')

print(sim)

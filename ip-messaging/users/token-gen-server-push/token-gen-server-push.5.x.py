from twilio.access_token import IpMessagingGrant

endpoint = 'https://end.point'
service_sid = 'ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

ipm_grant = IpMessagingGrant(
    endpoint_id=endpoint,
    service_sid=service_sid,
    push_credential_sid='CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print(ipm_grant)

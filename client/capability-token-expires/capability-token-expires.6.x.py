from twilio.util import ClientCapabilityToken

capability = ClientCapabilityToken('account_sid', 'auth_token')
token = capability.to_jwt()

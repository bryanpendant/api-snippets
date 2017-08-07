from twilio.util import TwilioCapability

capability = TwilioCapability('account_sid', 'auth_token')
token = capability.generate(expires=600)

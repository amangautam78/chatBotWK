from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#credentials
api_key = 'OHX_c7dqo8m5b0sNiMDfcnjVZKB5Yg6AMNcRZm3BkcSD'
url = 'https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/2b440ba5-99ad-4e26-8d74-50e31b9774e2'
assistant_id = '727f5913-615b-4208-8303-672c2e79f73b'

#Authentication
authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2020-09-24',
    authenticator=authenticator)
assistant.set_service_url(url)

def get_message(text):
    response = assistant.message_stateless(
        assistant_id = assistant_id,
        input = {
            "message":"text",
            "text":text}).get_result()
    response = response['output']['generic'][0]['text']
    return response


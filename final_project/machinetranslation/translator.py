from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def en_fr(txt):
    if txt is None:
        return None
    translation = language_translator.translate(
        text=txt,
        source='en',
        target='fr').get_result()
    return translation.get("translations")[0].get("translation")

def fr_en(txt):
    if txt is None:
        return None
    translation = language_translator.translate(
    text=txt,
    source='fr',
    target='en').get_result()
    return translation.get("translations")[0].get("translation")

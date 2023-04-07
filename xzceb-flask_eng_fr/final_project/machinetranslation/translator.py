"""
This module provides functions for translating text from English to French and vice versa
using the IBM Watson Language Translator service.
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

# Create an instance of the Watson Language Translator
authenticator = IAMAuthenticator('rlmiWfMPQSMSLmMRvMaly59_djZSzShwuNaGU7SPO4eV')
language_translator = LanguageTranslatorV3(
    version='2023-01-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/87a38be4-6d1f-4f28-90e2-baae62099844')


def english_to_french(english_text):
    if english_text:
        translation = language_translator.translate(
            text=english_text,
            source='en',
            target='fr'
        ).get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    else:
        return ''

def french_to_english(french_text):
    if french_text:
        translation = language_translator.translate(
            text=french_text,
            source='fr',
            target='en'
        ).get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    else:
        return ''
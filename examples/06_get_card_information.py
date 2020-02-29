# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_banking import PodBanking

try:
    pod_banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, private_key_path=PRIVATE_KEY_PATH,
                             user_name=USER_NAME_WEB_SERVICE, sc_api_key=SC_API_KEY)

    print(pod_banking.get_card_information(source_card_number=CARD_NUMBER, destination_card_number=CARD_NUMBER2))
    # OUTPUT
    # رضا زارع#1295000000

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

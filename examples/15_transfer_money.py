# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_banking import PodBanking
from datetime import datetime

try:
    pod_banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, private_key_path=PRIVATE_KEY_PATH,
                             user_name=USER_NAME_WEB_SERVICE, sc_api_key=SC_API_KEY)

    amount = 100

    print(pod_banking.transfer_money(amount=amount, payment_id="123", source_deposit_number=SOURCE_DEPOSIT_NUMBER,
                                     destination_deposit_number=DESTINATION_DEPOSIT_NUMBER))
    # OUTPUT
    # 678783602
    print(pod_banking.last_raw_result())
    # OUTPUT
    # {'IsSuccess': True, 'Message': None, 'Data': '678783602', 'MessageCode': 0}


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_banking import PodBanking
from datetime import datetime

try:
    pod_banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, private_key_path=PRIVATE_KEY_PATH,
                             user_name=USER_NAME_WEB_SERVICE, sc_api_key=SC_API_KEY)

    print(pod_banking.get_deposit_balance())
    # OUTPUT
    # {
    #   "DepositNumber": "1001.800.00000.2",
    #   "Amounts": [
    #     {
    #       "Amount": 978000,
    #       "CurrencySwiftCode": "IRR",
    #       "CurrencyISOCode": 0,
    #       "CurrencyName": "ريال"
    #     }
    #   ],
    #   "WithdrawableAmounts": [
    #     {
    #       "Amount": 478000,
    #       "CurrencySwiftCode": "IRR",
    #       "CurrencyISOCode": 0,
    #       "CurrencyName": "ريال"
    #     }
    #   ]
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_banking import PodBanking
from datetime import datetime

try:
    pod_banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, private_key_path=PRIVATE_KEY_PATH,
                             user_name=USER_NAME_WEB_SERVICE, sc_api_key=SC_API_KEY)

    bill_number = "5115000000052"
    payment_id = "30000016"

    print(pod_banking.bill_payment_by_deposit(deposit_number=SOURCE_DEPOSIT_NUMBER, bill_number=bill_number,
                                              payment_id=payment_id))
    # OUTPUT
    # 05040000009#50000000029
    print(pod_banking.last_raw_result())
    # {
    #   "IsSuccess":True,
    #   "Message":"عملیات پرداخت قبض با موفقیت انجام شد.",
    #   "Data":"05040000009#50000000029",
    #   "MessageCode":5001
    # }

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

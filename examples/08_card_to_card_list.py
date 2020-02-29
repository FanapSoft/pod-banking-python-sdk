# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_banking import PodBanking
from datetime import datetime

try:
    pod_banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, private_key_path=PRIVATE_KEY_PATH,
                             user_name=USER_NAME_WEB_SERVICE, sc_api_key=SC_API_KEY)

    start_date = datetime.now().__format__("%Y/%m/%d")
    end_date = datetime.now().__format__("%Y/%m/%d")
    source_card_number = '5022291029516661'

    print(pod_banking.card_to_card_list(source_card_number=source_card_number, min_amount=0, max_amount=100000000,
                                        start_date=start_date, end_date=end_date))

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_banking import PodBanking
from datetime import datetime

try:
    pod_banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, private_key_path=PRIVATE_KEY_PATH,
                             user_name=USER_NAME_WEB_SERVICE, sc_api_key=SC_API_KEY)

    print(pod_banking.get_deposit_invoice(start_date="2019/12/15", end_date="2020/01/15",
                                          deposit_number=SOURCE_DEPOSIT_NUMBER))
    # OUTPUT
    # [
    #   {
    #     "TransactionDate": "1398/10/24 - 17:24:18.6713990",
    #     "DeptorAmount": 100,
    #     "CreditorAmount": 0,
    #     "Description": "DESCRIPTION",
    #     "DocNumber": "1-98-1001-IRR-123456789",
    #     "ChqNumber": "",
    #     "Amount": 123456,
    #     "PaymentId": "1",
    #     "BranchCode": "1",
    #     "BranchName": "ستاد",
    #     "TransactionCode": "*************************************************",
    #     "TransactionSideLastName": "",
    #     "TransactionSideFirstName": "",
    #     "TransactionSideDestDepositNum": "",
    #     "TransactionSideSrcDepositNum": ""
    #   },
    #   ...
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

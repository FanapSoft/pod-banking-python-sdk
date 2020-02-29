# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_banking import PodBanking
from datetime import datetime

try:
    pod_banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, private_key_path=PRIVATE_KEY_PATH,
                             user_name=USER_NAME_WEB_SERVICE, sc_api_key=SC_API_KEY)

    batch_paya_items = [
        {
            'Amount': 100,
            'BeneficiaryFullName': 'رضا زارع',
            'Description': 'تست ارسال از طریق پایتون',
            'DestShebaNumber': 'IR************************',
            'BillNumber': datetime.now().__format__("%s")+"1"
        },
        {
            'Amount': 100,
            'BeneficiaryFullName': 'رضا زارع',
            'Description': 'تست ارسال از طریق پایتون',
            'DestShebaNumber': 'IR************************',
            'BillNumber': datetime.now().__format__("%s")+"2"
        }
    ]

    print(pod_banking.paya_service(source_deposit_number=SOURCE_DEPOSIT_NUMBER,
                                   file_unique_identifier='ACH'+datetime.now().__format__("%s"),
                                   batch_paya_item_infos=batch_paya_items))
    # OUTPUT
    # [
    #   {
    #     "ReferenceNumber": "****************",
    #     "DestinationBankName": "پاسارگاد",
    #     "State": "ثبت و واریز شده",
    #     "BatchNumber": **********,
    #     "BatchTransferId": ******,
    #     "Amount": 100,
    #     "BeneficiaryFullName": "رضا زارع",
    #     "Description": "تست ارسال از طريق پايتون",
    #     "DestShebaNumber": "IR************************",
    #     "BillNumber": "1582************",
    #     "InquiryName": ""
    #   },
    #   {
    #     "ReferenceNumber": "****************",
    #     "DestinationBankName": "ملي",
    #     "State": "ثبت شده",
    #     "BatchNumber": **********,
    #     "BatchTransferId": ******,
    #     "Amount": 100,
    #     "BeneficiaryFullName": "رضا زارع",
    #     "Description": "تست ارسال از طريق پايتون",
    #     "DestShebaNumber": "IR************************",
    #     "BillNumber": "1582************",
    #     "InquiryName": ""
    #   }
    # ]

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)

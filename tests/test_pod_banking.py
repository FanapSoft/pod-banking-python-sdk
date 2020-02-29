# coding=utf-8
from __future__ import unicode_literals

import unittest
from datetime import datetime
from sys import version_info

from pod_base import InvalidDataException, APIException

from pod_banking import PodBanking
from tests.config import *


class TestPodBanking(unittest.TestCase):
    __slots__ = "__banking"

    def setUp(self):
        self.__banking = PodBanking(api_token=API_TOKEN, server_type=SERVER_MODE, user_name=USER_NAME_WEB_SERVICE,
                                    sc_api_key=SC_API_KEY, private_key_path=PRIVATE_KEY_PATH)

    def test_01_get_sheba_info(self):
        result = self.__banking.get_sheba_info(sheba=SHEBA_NUMBER)
        self.assertIsInstance(result, dict, msg="get sheba info : check instance")
        self.assertEqual(result["sheba"], SHEBA_NUMBER, msg="get sheba info : check equal sheba")

    def test_01_get_sheba_info_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get sheba info : validation error"):
            self.__banking.get_sheba_info(sheba="ASDASDASD")

    def test_01_get_sheba_info_required_params(self):
        with self.assertRaises(TypeError, msg="get sheba info : required params"):
            self.__banking.get_sheba_info()

    def test_02_get_debit_card_info(self):
        result = self.__banking.get_debit_card_info(card_number=CARD_NUMBER)
        self.assertIsInstance(result, str, msg="get debit card info : check instance")

    def test_02_get_debit_card_info_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get debit card info : validation error"):
            self.__banking.get_debit_card_info(card_number="456456")

    def test_02_get_debit_card_info_required_params(self):
        with self.assertRaises(TypeError, msg="get debit card info : required params"):
            self.__banking.get_debit_card_info()

    def test_03_get_sheba_info_and_status(self):
        result = self.__banking.get_sheba_info_and_status(sheba=SHEBA_NUMBER)
        self.assertIsInstance(result, dict, msg="get sheba info : check instance")
        self.assertEqual(result["Sheba"], SHEBA_NUMBER, msg="get sheba info : check equal sheba")

    def test_03_get_sheba_info_and_status_all_params(self):
        result = self.__banking.get_sheba_info_and_status(sheba=SHEBA_NUMBER, shenase_variz="123456")
        self.assertIsInstance(result, dict, msg="get sheba info (all params): check instance")
        self.assertEqual(result["Sheba"], SHEBA_NUMBER, msg="get sheba info (all params): check equal sheba")

    def test_03_get_sheba_info_and_status_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get sheba info : validation error"):
            self.__banking.get_sheba_info_and_status(sheba="ASDASDASD")

    def test_03_get_sheba_info_and_status_required_params(self):
        with self.assertRaises(TypeError, msg="get sheba info : required params"):
            self.__banking.get_sheba_info_and_status()

    def test_04_get_deposit_number_by_card_number(self):
        result = self.__banking.get_deposit_number_by_card_number(card_number=CARD_NUMBER)
        if version_info[0] == 2:
            self.assertIsInstance(result, unicode, msg="get deposit number by card number : check instance")
        else:
            self.assertIsInstance(result, str, msg="get deposit number by card number : check instance")

    def test_04_get_deposit_number_by_card_number_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get deposit number by card number : validation error"):
            self.__banking.get_deposit_number_by_card_number(card_number="ASDASDASD")

    def test_04_get_deposit_number_by_card_number_required_params(self):
        with self.assertRaises(TypeError, msg="get deposit number by card number : required params"):
            self.__banking.get_deposit_number_by_card_number()

    def test_05_get_sheba_by_card_number(self):
        result = self.__banking.get_sheba_by_card_number(card_number=CARD_NUMBER)
        if version_info[0] == 2:
            self.assertIsInstance(result, unicode, msg="get deposit number by card number : check instance")
        else:
            self.assertIsInstance(result, str, msg="get deposit number by card number : check instance")

    def test_05_get_sheba_by_card_number_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get deposit number by card number : validation error"):
            self.__banking.get_sheba_by_card_number(card_number="ASDASDASD")

    def test_05_get_sheba_by_card_number_required_params(self):
        with self.assertRaises(TypeError, msg="get deposit number by card number : required params"):
            self.__banking.get_sheba_by_card_number()

    def test_06_get_card_information(self):
        result = self.__banking.get_card_information(source_card_number=CARD_NUMBER,
                                                     destination_card_number=CARD_NUMBER2)
        if version_info[0] == 2:
            self.assertIsInstance(result, unicode, msg="get card information : check instance")
        else:
            self.assertIsInstance(result, str, msg="get card information : check instance")

    def test_06_get_card_information_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get card information : validation error"):
            self.__banking.get_card_information(source_card_number="ASDASDASD", destination_card_number="sad")

    def test_06_get_card_information_required_params(self):
        with self.assertRaises(TypeError, msg="get card information : required params"):
            self.__banking.get_card_information()

    def test_07_card_to_card(self):
        try:
            result = self.__banking.card_to_card(source_card_number=CARD_NUMBER, destination_card_number=CARD_NUMBER2,
                                                 cvv2="133", password="12345", expire_month="06", expire_year="03",
                                                 amount=2000000)
            self.assertIsInstance(result, str, msg="card to card : check instance")
        except APIException as e:
            self.assertEqual(e.error_code, 6032, msg="card to card : check error code")

    def test_07_card_to_card_all_params(self):
        try:
            result = self.__banking.card_to_card(source_card_number=CARD_NUMBER, destination_card_number=CARD_NUMBER2,
                                                 cvv2="133", password="12345", expire_month="06", expire_year="03",
                                                 amount=2000000, email="email@google.com", card_name="test")
            self.assertIsInstance(result, str, msg="card to card (all params) : check instance")
        except APIException as e:
            self.assertEqual(e.error_code, 6032, msg="card to card : check error code")

    def test_07_card_to_card_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="card to card : validation error"):
            self.__banking.card_to_card(source_card_number="ASDASD", destination_card_number="ASDASD",
                                        cvv2="133", password="12345", expire_month="06", expire_year="03",
                                        amount=2000000)

    def test_07_card_to_card_required_params(self):
        with self.assertRaises(TypeError, msg="card to card : required params"):
            self.__banking.card_to_card()

    def test_08_card_to_card_list(self):
        try:
            result = self.__banking.card_to_card_list(source_card_number=CARD_NUMBER, min_amount=0, max_amount=100000,
                                                      start_date="2019/12/15", end_date="2019/12/30")
            self.assertIsInstance(result, list, msg="card to card list : check instance")
        except APIException as e:
            self.assertEqual(e.error_code, 3015, msg="card to card list (all params) : check error code")

    def test_08_card_to_card_list_all_params(self):
        try:
            result = self.__banking.card_to_card_list(source_card_number=CARD_NUMBER, min_amount=0, max_amount=100000,
                                                      start_date="2019/12/15", end_date="2019/12/30",
                                                      source_deposit_number=SOURCE_DEPOSIT_NUMBER,
                                                      destination_card_number=DESTINATION_DEPOSIT_NUMBER,
                                                      sequence_number="123", reference_number="123", source_note="abcd",
                                                      destination_note="abcd")
            self.assertIsInstance(result, list, msg="card to card list (all params) : check instance")
        except APIException as e:
            self.assertEqual(e.error_code, 3015, msg="card to card list (all params) : check error code")

    def test_08_card_to_card_list_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="card to card list : validation error"):
            self.__banking.card_to_card_list(source_card_number="asdasdasd", min_amount="0", max_amount="100000",
                                             start_date="2019_12_15", end_date="2019_12_30",
                                             source_deposit_number="asd.4654",
                                             destination_card_number="56456456464654564",
                                             sequence_number="123", reference_number="123", source_note="abcd",
                                             destination_note="abcd")

    def test_08_card_to_card_list_required_params(self):
        with self.assertRaises(TypeError, msg="card to card list : required params"):
            self.__banking.card_to_card_list()

    def test_09_get_submission_cheque(self):
        result = self.__banking.get_submission_cheque(deposit=SOURCE_DEPOSIT_NUMBER)
        self.assertIsInstance(result, list, msg="get submission cheque : check instance")

    def test_09_get_submission_cheque_all_params(self):
        result = self.__banking.get_submission_cheque(deposit=SOURCE_DEPOSIT_NUMBER, min_amount=1000, max_amount=200000,
                                                      start_date="2019/12/15", end_date="2019/12/30",
                                                      start_submission_date="2019/12/01",
                                                      end_submission_date="2019/12/30", cheque_number="123456789",
                                                      row_count=10, bank_code=55, cheque_status=2)
        self.assertIsInstance(result, list, msg="get submission cheque (all params) : check instance")

    def test_09_get_submission_cheque_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get submission cheque : validation error"):
            self.__banking.get_submission_cheque(deposit=SOURCE_DEPOSIT_NUMBER, min_amount="1000", max_amount="200000",
                                                 start_date="2019_12_15", end_date="2019_12_30",
                                                 start_submission_date="2019_12_01",
                                                 end_submission_date="2019_12_30", cheque_number="123456789",
                                                 row_count="10", bank_code="55", cheque_status="2")

    def test_09_get_submission_cheque_required_params(self):
        with self.assertRaises(TypeError, msg="get submission cheque : required params"):
            self.__banking.get_submission_cheque()

    def test_10_convert_deposit_number_to_sheba(self):
        result = self.__banking.convert_deposit_number_to_sheba(deposit_number=DESTINATION_DEPOSIT_NUMBER)
        if version_info[0] == 2:
            self.assertIsInstance(result, unicode, msg="convert deposit number to sheba : check instance")
        else:
            self.assertIsInstance(result, str, msg="convert deposit number to sheba : check instance")

    def test_10_convert_deposit_number_to_sheba_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="convert deposit number to sheba : validation error"):
            self.__banking.convert_deposit_number_to_sheba(deposit_number=123456)

    def test_10_convert_deposit_number_to_sheba_required_params(self):
        with self.assertRaises(TypeError, msg="convert deposit number to sheba : required params"):
            self.__banking.convert_deposit_number_to_sheba()

    def test_11_convert_sheba_to_deposit_number(self):
        result = self.__banking.convert_sheba_to_deposit_number(sheba=SHEBA_NUMBER)
        if version_info[0] == 2:
            self.assertIsInstance(result, unicode, msg="convert deposit number to sheba : check instance")
        else:
            self.assertIsInstance(result, str, msg="convert deposit number to sheba : check instance")

    def test_11_convert_sheba_to_deposit_number_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="convert deposit number to sheba : validation error"):
            self.__banking.convert_sheba_to_deposit_number(sheba="123456")

    def test_11_convert_sheba_to_deposit_number_required_params(self):
        with self.assertRaises(TypeError, msg="convert deposit number to sheba : required params"):
            self.__banking.convert_sheba_to_deposit_number()

    def test_12_paya_service(self):
        batch_paya_items = [
            {
                "Amount": 100,
                "BeneficiaryFullName": "نام و نام خانوادگی",
                "Description": "تست ارسال از طریق پایتون",
                "DestShebaNumber": DESTINATION_SHEBA_NUMBER,
                "BillNumber": datetime.now().__format__("%s%f")
            }
        ]
        result = self.__banking.paya_service(source_deposit_number=SOURCE_DEPOSIT_NUMBER,
                                             batch_paya_item_infos=batch_paya_items)
        self.assertIsInstance(result, list, msg="paya service : check instance")

    def test_12_paya_service_validation_error(self):
        batch_paya_items = [
            {
                "Amount": 100,
                "BeneficiaryFullName": "رضا زارع",
                "Description": "unit testing python",
                "DestShebaNumber": "IR8789787"
            },
            {
                "Amount": 100,
                "BeneficiaryFullName": "رضا زارع",
                "Description": "unit testing python"
            }
        ]

        with self.assertRaises(InvalidDataException, msg="paya service : validation error"):
            self.__banking.paya_service(source_deposit_number=123132,
                                        file_unique_identifier='ACH1582358228780770',
                                        batch_paya_item_infos=batch_paya_items)

    def test_12_paya_service_required_params(self):
        with self.assertRaises(TypeError, msg="paya service : required params"):
            self.__banking.paya_service()

    def test_13_get_deposit_invoice_by_sheba(self):
        result = self.__banking.get_deposit_invoice(start_date="2019/12/15", end_date="2019/12/30", sheba=SHEBA_NUMBER)
        self.assertIsInstance(result, list, msg="get deposit invoice by sheba : check instance")

    def test_13_get_deposit_invoice_by_deposit_number(self):
        result = self.__banking.get_deposit_invoice(start_date="2019/12/15", end_date="2019/12/30",
                                                    deposit_number=SOURCE_DEPOSIT_NUMBER)
        self.assertIsInstance(result, list, msg="get deposit invoice by deposit number : check instance")

    def test_13_get_deposit_invoice_all_params(self):
        result = self.__banking.get_deposit_invoice(start_date="2019/12/15", end_date="2019/12/30",
                                                    deposit_number=SOURCE_DEPOSIT_NUMBER, count=10, first_index=10)
        self.assertIsInstance(result, list, msg="get deposit invoice (all params) : check instance")

    def test_13_get_deposit_invoice_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get deposit invoice : validation error"):
            self.__banking.get_deposit_invoice(start_date="2019_12_15", end_date="2019_12_30", sheba="4564")

    def test_13_get_deposit_invoice_required_params(self):
        with self.assertRaises(TypeError, msg="get deposit invoice : required params"):
            self.__banking.get_deposit_invoice()

    def test_14_get_deposit_balance_by_deposit_number(self):
        result = self.__banking.get_deposit_balance(deposit_number=SOURCE_DEPOSIT_NUMBER)
        self.assertIsInstance(result, dict, msg="get deposit balance by deposit number : check instance")

    def test_14_get_deposit_balance_by_sheba(self):
        result = self.__banking.get_deposit_balance(sheba=SHEBA_NUMBER)
        self.assertIsInstance(result, dict, msg="get deposit balance by sheba : check instance")

    def test_14_get_deposit_balance_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="get deposit balance : validation error"):
            self.__banking.get_deposit_balance(sheba="asdasd")

    def test_14_get_deposit_balance_required_params(self):
        with self.assertRaises(InvalidDataException, msg="get deposit balance : required params"):
            self.__banking.get_deposit_balance()

    def test_15_transfer_money(self):
        payment_id = datetime.now().__format__("%s")
        result = self.__banking.transfer_money(amount=100, payment_id=payment_id,
                                               source_deposit_number=SOURCE_DEPOSIT_NUMBER,
                                               destination_deposit_number=DESTINATION_DEPOSIT_NUMBER)
        if version_info[0] == 2:
            self.assertIsInstance(result, unicode, msg="transfer money : check instance")
        else:
            self.assertIsInstance(result, str, msg="transfer money : check instance")

    def test_15_transfer_money_all_params(self):
        payment_id = datetime.now().__format__("%s")
        result = self.__banking.transfer_money(amount=100, payment_id=payment_id,
                                               source_sheba=SHEBA_NUMBER,
                                               destination_deposit_number=DESTINATION_DEPOSIT_NUMBER,
                                               source_comment="تست پایتون",
                                               destination_comment="انتقال از طریق تست پایتون")
        if version_info[0] == 2:
            self.assertIsInstance(result, unicode, msg="transfer money (all params): check instance")
        else:
            self.assertIsInstance(result, str, msg="transfer money (all params): check instance")

    def test_15_transfer_money_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="transfer money : validation error"):
            self.__banking.transfer_money(amount="100", payment_id="123",
                                          source_deposit_number="asdasd",
                                          destination_deposit_number="asdsdas")

    def test_15_transfer_money_required_params(self):
        with self.assertRaises(TypeError, msg="transfer money : required params"):
            self.__banking.transfer_money()

    def test_16_get_transfer_state(self):
        result = self.__banking.get_transfer_state(payment_id="123", date="2020/02/23")
        self.assertIsInstance(result, dict, msg="transfer money : check instance")

    def test_16_get_transfer_state_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="transfer money : validation error"):
            self.__banking.get_transfer_state(payment_id=123, date="2020_02_23")

    def test_16_get_transfer_state_required_params(self):
        with self.assertRaises(TypeError, msg="transfer money : required params"):
            self.__banking.get_transfer_state()

    def test_17_bill_payment_by_deposit(self):
        try:
            bill_number = "5115000000052"
            payment_id = "30000016"

            result = self.__banking.bill_payment_by_deposit(deposit_number=SOURCE_DEPOSIT_NUMBER,
                                                            bill_number=bill_number, payment_id=payment_id)
            self.assertIsInstance(result, str, msg="bill payment by deposit : check instance")
        except APIException as e:
            self.assertEqual(e.error_code, 6043, msg="bill payment by deposit : check error code")

    def test_17_bill_payment_by_deposit_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="bill payment by deposit : validation error"):
            self.__banking.bill_payment_by_deposit(deposit_number=123456,
                                                   bill_number="asdasd", payment_id="sadasd")

    def test_17_bill_payment_by_deposit_required_params(self):
        with self.assertRaises(TypeError, msg="bill payment by deposit : required params"):
            self.__banking.bill_payment_by_deposit()

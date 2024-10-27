from config import config
from src.generated_data.bdvo.payement_bdvo_swift_transfer import SwiftTransfer
from src.generated_data.bdvo.payment_bdvo_operation import Operation
from src.generated_data.bdvo.payment_bdvo_payer import Payer
from src.generated_data.bdvo.payment_bdvo_payee import Payee
from src.generated_data.bdvo.payment_bdvo_correspondence import Correspondece
from src.generated_data.bdvo.payment_bdvo_object_versions import ObjectVersions
import random

class PaymentBDVO:
    def __init__(self, direction: str, creator_system: str = None):
        self.swiftTransfer: SwiftTransfer = SwiftTransfer()
        self.operation: Operation = Operation()
        self.payer: Payer = Payer()
        self.payee: Payee = Payee()
        self.correspondence: Correspondece = Correspondece()
        self.objectVersions: ObjectVersions = ObjectVersions()
        
    

        
    def create_direction(self, direction: str, creator_system: str):
        pass

    @staticmethod
    def create_account(is_resident: bool = True,
                       is_transint: bool = False,
                       account_lenght: int = 20,
                       currency_code: str = '810',
                       is_client_acccount: bool = True
                       ):
        if is_resident:
            start_account_list = config.account_resident_masks
        else:
            start_account_list = config.account_not_resident_masks
        start_account_value = str(start_account_list[random.randint(0, len(start_account_list)-1)])


        if len(start_account_value) != 5:
            for item in range(0, 4):
                start_account_value += str(item)
                if len(start_account_value) == 5:
                    break

        if currency_code in config.dict_currency.keys():
            currency_code = config.dict_currency[currency_code]

        third_part_account = str(random.randint(10000,19999))

        transit_value = '00'
        if is_transint:
            transit_value = '10' if random.randint(0,1) == 0 else '02'

        last_part_account = ''
        for item in range(0, account_lenght - 15):
            last_part_account += str(random.randint(0,9))

        return start_account_value + currency_code + third_part_account + transit_value + last_part_account

    def get_swiftTransfer(self):
        return self.swiftTransfer

    def set_swiftTransfer(self, value):
        self.swiftTransfer = value

    def get_operation(self):
        return self.operation

    def set_operation(self, value):
        self.operation = value

    def get_payer(self):
        return self.payer

    def set_payer(self, value):
        self.payer = value

    def get_payee(self):
        return self.payee

    def set_payee(self, value):
        self.payee = value

    def get_correspondence(self):
        return self.correspondence

    def set_correspondence(self, value):
        self.correspondence = value

    def get_objectVersions(self):
        return self.objectVersions

    def set_objectVersions(self, value):
        self.objectVersions = value

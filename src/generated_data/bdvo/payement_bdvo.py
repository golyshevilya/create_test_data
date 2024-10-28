from config import config
from src.generated_data.bdvo.payement_bdvo_swift_transfer import SwiftTransfer
from src.generated_data.bdvo.payment_bdvo_operation import Operation
from src.generated_data.bdvo.payment_bdvo_payer import Payer
from src.generated_data.bdvo.payment_bdvo_payee import Payee
from src.generated_data.bdvo.payment_bdvo_correspondence import Correspondece
from src.generated_data.bdvo.payment_bdvo_object_versions import ObjectVersions
import random
import itertools
import faker
import json

class PaymentBDVO:
    def __init__(self, **kwargs):
        kwargs = kwargs['kwargs']
        self.__faker__ = faker.Faker()
        
        self.__customer_account__ = self.create_account(
            is_resident=self.create_is_resident(customer=kwargs['customer']),
            is_transint=self.create_is_transit(is_transit=kwargs['is_transit_customer_account']),
            account_lenght=20,
            currency_code=self.create_customer_currency(customer_currency=kwargs['customer_currency']),
            is_client_acccount=True
        )
        
        self.__customer_name__ = self.create_person_name()
        self.__customer_inn__ = self.create_inn()
        self.__customer_bank_name__ = random.choice(config.bank_names)
        self.__customer_bank_swift__ = self.__faker__.swift()
        self.__customer_bank_bic__ = random.randint(100000000, 999999999)
        self.__currency_operation_code__ = self.create_currency_operation_code(kwargs['currency_operation_code'])
        self.__is_registry__ = self.create_is_registry(is_registry=kwargs['is_registry'])
        self.__operation__purpose__ = self.create_purpose(is_vo_code=False if random.randint(0,1)==0 else True, is_registry=self.__is_registry__)
        self.__document_number__ = random.randint(100000, 999999999)
        self.__document_date__ = str(self.__faker__.date_between(start_date='-10d', end_date='now'))
        
        
        self.swiftTransfer: SwiftTransfer = SwiftTransfer(
            sender_system=kwargs['sender_system'],
            customer_account=self.__customer_account__,
            customer_name=self.__customer_name__,
            customer_inn=self.__customer_inn__,
            customer_bank_name=self.__customer_bank_name__,
            customer_bank_swift=self.__customer_bank_swift__,
            customer_bic=self.__customer_bank_bic__,
            operation_purpose=self.__operation__purpose__,
            documnet_number=self.__document_number__, 
            document_date=self.__document_date__
        )
        self.operation: Operation = Operation()
        self.payer: Payer = Payer()
        self.payee: Payee = Payee()
        self.correspondence: Correspondece = Correspondece()
        self.objectVersions: ObjectVersions = ObjectVersions()
        
        
    def to_JSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
    
    @staticmethod    
    def create_is_registry(is_registry: str):
        if is_registry == 'рандом':
            return True if random.randint(0,1) == 0 else False
        elif is_registry == 'да':
            return True
        else:
            return False
    
    @staticmethod
    def create_currency_operation_code(currency_operation_code: str):
        if currency_operation_code == 'рандом':
            return str(random.randint(10000, 99999))
        else: 
            return currency_operation_code
        
    
    def create_purpose(self, is_vo_code: bool = False, is_registry: bool = False):
        result = ''
        if is_vo_code:
            result += random.choice(
                [
                    '{VO%s} ' % self.__currency_operation_code__,
                    '{V0%s} ' % self.__currency_operation_code__,
                    '(VO%s) ' % self.__currency_operation_code__,
                    '(V0%s) ' % self.__currency_operation_code__,
                ]
            )
        
        if is_registry:
            result += 'Операция по реестру № ' + str(random.randint(10000, 99999))
            result += ' от ' + str(self.__faker__.date_between(start_date='-10y', end_date='now'))
            result += ' в соответсвии с Договором ' + str(random.randint(100000000, 9999999999))
            result += ' от ' + str(self.__faker__.date_between(start_date='-5d', end_date='now'))
        else:
            result += 'Оплата по договору № ' + str(random.randint(10000, 99999)) 
            result += ' от ' + str(self.__faker__.date_between(start_date='-10y', end_date='now'))
            result += ' за товар или услугу. МБ с НДС мб без'
        
        return result
            
    
    @staticmethod    
    def inn_ctrl_summ(nums, type):
        """
        Подсчет контрольной суммы
        """
        inn_ctrl_type = {
            'n2_12': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
        }
        n = 0
        l = inn_ctrl_type[type]
        for i in range(0, len(l)):
            n += nums[i] * l[i]
        return n % 11 % 10
        
    
    def create_inn(self, lenght_inn: int = None):
        if not lenght_inn:
            lenght_inn = list((10, 12))[random.randint(0, 1)]
            if lenght_inn not in (10, 12):
                return None
            nums = [
                random.randint(1, 9) if x == 0
                else random.randint(0, 9)
                for x in range(0, 9 if lenght_inn == 10 else 10)
            ]
            if lenght_inn == 12:
                n2 = self.inn_ctrl_summ(nums, 'n2_12')
                nums.append(n2)
                n1 = self.inn_ctrl_summ(nums, 'n1_12')
                nums.append(n1)
            elif lenght_inn == 10:
                n1 = self.inn_ctrl_summ(nums, 'n1_10')
                nums.append(n1)
            return ''.join([str(x) for x in nums])
    

    @staticmethod
    def create_person_name():
        return random.choice(config.list_legal_forms) + ' ' + '"' + random.choice(config.list_legal_names) + '"'
    
    @staticmethod
    def create_customer_currency(customer_currency: str):
        if customer_currency == 'рандом':
            return random.choice(list(config.dict_currency.values()))
        elif customer_currency == 'рубли':
            return '810'
        else: 
            return random.choice(itertools.islice(config.dict_currency.values(), len(config.dict_currency)-2))

        
    @staticmethod
    def create_is_transit(is_transit: str):
        if is_transit == 'рандом':
            return True if random.randint(0,1) == 0 else False
        elif is_transit == 'резидент':
            return True
        else:
            return False

    @staticmethod
    def create_is_resident(customer: str):
        if customer == 'рандом':
            return True if random.randint(0,1) == 0 else False
        elif customer == 'резидент':
            return True
        else:
            return False
        
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
        if is_client_acccount:
            account_lenght = 20
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

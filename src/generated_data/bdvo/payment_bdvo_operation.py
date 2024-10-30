import faker
import datetime
import random

class Operation:
    def __init__(self, 
                 document_date: str, 
                 document_number: str,
                 document_amount: float,
                 document_currency: str,
                 document_currency_code: int,
                 amount_national: float,
                 purpose: str,
                 currency_operation_code: str,
                 divisionId: str,
                 direction: str,
                 payment_code: str
                ):
        
        self.__faker__ = faker.Faker()
        
        self.status = random.choice(['EXECUTED', 'REJECTED', 'SENT_EKS'])
        self.date: str = datetime.datetime.today().strftime('%Y-%m-%d')
        self.documentDate: str = document_date
        self.documentNumber: str = document_number
        self.documentAmount: float = document_amount
        self.documentCurrencyCode: int = document_currency_code
        self.documentCurrency: str = document_currency
        self.amountNational: float = amount_national
        self.purpose: str = purpose
        self.purposeCode: str = random.randint(1, 100000)
        self.voCode: str = currency_operation_code
        self.payingCondition: str = None
        self.payingConditionDate: str = None
        self.bankBranchCode, self.departmentCode = divisionId[0:2], divisionId
        self.direction: int = direction
        self.paymentCode: str = payment_code
        self.receiptDateToBank: str = str(self.__faker__.date_between(start_date='-1d', end_date='now'))


    def to_JSON(self):
        result_dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith('__') and not callable(key):
                try:
                    result_dict[key] = value.to_JSON()
                except:
                    result_dict[key] = value
                    continue
        return result_dict
    
    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_date(self):
        return self.date

    def set_date(self, value):
        self.date = value

    def get_documentDate(self):
        return self.documentDate

    def set_documentDate(self, value):
        self.documentDate = value

    def get_documentNumber(self):
        return self.documentNumber

    def set_documentNumber(self, value):
        self.documentNumber = value

    def get_documentAmount(self):
        return self.documentAmount

    def set_documentAmount(self, value):
        self.documentAmount = value

    def get_documentCurrencyCode(self):
        return self.documentCurrencyCode

    def set_documentCurrencyCode(self, value):
        self.documentCurrencyCode = value

    def get_documentCurrency(self):
        return self.documentCurrency

    def set_documentCurrency(self, value):
        self.documentCurrency = value

    def get_amountNational(self):
        return self.amountNational

    def set_amountNational(self, value):
        self.amountNational = value

    def get_purpose(self):
        return self.purpose

    def set_purpose(self, value):
        self.purpose = value

    def get_purposeCode(self):
        return self.purposeCode

    def set_purposeCode(self, value):
        self.purposeCode = value

    def get_voCode(self):
        return self.voCode

    def set_voCode(self, value):
        self.voCode = value

    def get_payingCondition(self):
        return self.payingCondition

    def set_payingCondition(self, value):
        self.payingCondition = value

    def get_payingConditionDate(self):
        return self.payingConditionDate

    def set_payingConditionDate(self, value):
        self.payingConditionDate = value

    def get_bankBranchCode(self):
        return self.bankBranchCode

    def set_bankBranchCode(self, value):
        self.bankBranchCode = value

    def get_departmentCode(self):
        return self.departmentCode

    def set_departmentCode(self, value):
        self.departmentCode = value

    def get_direction(self):
        return self.direction

    def set_direction(self, value):
        self.direction = value

    def get_paymentCode(self):
        return self.paymentCode

    def set_paymentCode(self, value):
        self.paymentCode = value

    def get_receiptDateToBank(self):
        return self.receiptDateToBank

    def set_receiptDateToBank(self, value):
        self.receiptDateToBank = value

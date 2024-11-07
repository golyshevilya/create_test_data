import abc
import datetime

import faker


class OperationAbstract(abc.ABC):

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
                 payment_code: str):
		self.__faker__ = faker.Faker()
		self.status = None
		self.date: str = datetime.datetime.today().strftime('%Y-%m-%d')
		self.documentDate: str = document_date
		self.documentNumber: str = document_number
		self.documentAmount: float = document_amount
		self.documentCurrencyCode: int = document_currency_code
		self.documentCurrency: str = document_currency
		self.amountNational: float = amount_national
		self.purpose: str = purpose
		self.voCode: str = currency_operation_code
		self.payingCondition: str = None
		self.payingConditionDate: str = None
		self.bankBranchCode, self.departmentCode = divisionId[0:2], divisionId
		self.direction: int = direction
		self.paymentCode: str = payment_code
		self.purposeCode = None
		self.receiptDateToBank = None

	def __deepcopy__(self, memo):
		return

	def to_JSON(self):
		result_dict = {}
		for key, value in self.__dict__.items():
			if not key.startswith('__') and not callable(key):
				try:
					result_dict[key] = value.to_JSON
				except:
					result_dict[key] = value
					continue
		return result_dict
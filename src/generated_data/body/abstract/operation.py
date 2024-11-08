import abc
import copy
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
		return OperationAbstract(
			document_date=copy.deepcopy(self.documentDate, memo=memo),
			document_number=copy.deepcopy(self.documentNumber, memo=memo),
			document_amount=copy.deepcopy(self.documentAmount, memo=memo),
			document_currency=copy.deepcopy(self.documentCurrency, memo=memo),
			document_currency_code=copy.deepcopy(self.documentCurrencyCode, memo=memo),
			amount_national=copy.deepcopy(self.amountNational, memo=memo),
			purpose=copy.deepcopy(self.purpose, memo=memo),
			currency_operation_code=copy.deepcopy(self.voCode, memo=memo),
			divisionId=copy.deepcopy(self.bankBranchCode, memo=memo),
			direction=copy.deepcopy(self.direction, memo=memo),
			payment_code=copy.deepcopy(self.paymentCode, memo=memo)
		)

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
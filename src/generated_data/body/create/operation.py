import random

from src.generated_data.body.abstract.operation import OperationAbstract


class OperationCreate(OperationAbstract):
	def __init__(self, document_date: str, document_number: str, document_amount: float, document_currency: str,
	             document_currency_code: int, amount_national: float, purpose: str, currency_operation_code: str,
	             divisionId: str, direction: str, payment_code: str):
		super().__init__(document_date, document_number, document_amount, document_currency, document_currency_code,
		                 amount_national, purpose, currency_operation_code, divisionId, direction, payment_code)
		self.set_paymentCode(random.randint(1, 100000))
		self.set_receiptDateToBank(str(self.__faker__.date_between(start_date = '-1d', end_date = 'now')))

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

import copy
import random

from config import config
from src.generated_data.body.abstract.operation import OperationAbstract


class OperationUpdate(OperationAbstract):
	def __init__(self, document_date: str, document_number: str, document_amount: float, document_currency: str,
	             document_currency_code: int, amount_national: float, purpose: str, currency_operation_code: str,
	             divisionId: str, direction: str, payment_code: str):
		super().__init__(document_date, document_number, document_amount, document_currency, document_currency_code,
		                 amount_national, purpose, currency_operation_code, divisionId, direction, payment_code)

	def __deepcopy__(self, memo):
		return OperationUpdate(
			document_date = copy.deepcopy(self.documentDate, memo = memo),
			document_number = copy.deepcopy(self.documentNumber, memo = memo),
			document_amount = copy.deepcopy(self.documentAmount, memo = memo),
			document_currency = copy.deepcopy(self.documentCurrency, memo = memo),
			document_currency_code = copy.deepcopy(self.documentCurrencyCode, memo = memo),
			amount_national = copy.deepcopy(self.amountNational, memo = memo),
			purpose = copy.deepcopy(self.purpose, memo = memo),
			currency_operation_code = copy.deepcopy(self.voCode, memo = memo),
			divisionId = copy.deepcopy(self.departmentCode, memo = memo),
			direction = copy.deepcopy(self.direction, memo = memo),
			payment_code = copy.deepcopy(self.paymentCode, memo = memo)
		)

	def update_documentDate(self):
		current_value = self.get_documentDate()
		new_value = str(self.__faker__.date_between(start_date = '-10d', end_date = 'now'))
		while current_value == new_value:
			new_value = str(self.__faker__.date_between(start_date = '-10d', end_date = 'now'))
		self.set_documentDate(new_value)

	def update_documentNumber(self):
		current_value = self.get_documentNumber()
		new_value = random.randint(100000, 999999999)
		while current_value == new_value:
			new_value = random.randint(100000, 999999999)
		self.set_documentNumber(new_value)

	def update_purpose(self):
		current_value = self.get_purpose()
		new_value = ''
		if self.get_voCode():
			new_value += random.choice(
				[
					'{VO%s} ' % self.get_voCode(),
					'{V0%s} ' % self.get_voCode(),
					'(VO%s) ' % self.get_voCode(),
					'(V0%s) ' % self.get_voCode(),
				]
			)

		if current_value.__contains__('Операция по реестру'):
			new_value += 'Операция по реестру № ' + str(random.randint(10000, 99999))
			new_value += ' от ' + str(self.__faker__.date_between(start_date = '-10y', end_date = 'now'))
			new_value += ' в соответствии с Договором ' + str(random.randint(100000000, 9999999999))
			new_value += ' от ' + str(self.__faker__.date_between(start_date = '-5d', end_date = 'now'))
		else:
			new_value += 'Оплата по договору № ' + str(random.randint(10000, 99999))
			new_value += ' от ' + str(self.__faker__.date_between(start_date = '-10y', end_date = 'now'))
			new_value += ' за товар или услугу. МБ с НДС мб без'


		self.set_purpose(new_value)

	def update_voCode(self):
		current_value = self.get_voCode()
		new_value = str(random.randint(10000, 99999))
		while current_value == new_value:
			new_value = str(random.randint(10000, 99999))
		self.set_voCode(new_value)

	def update_bankBranchCode(self):
		current_value = self.get_bankBranchCode()
		new_value = str(random.randint(10, 99))
		while current_value == new_value:
			new_value = str(random.randint(10, 99))
		self.set_bankBranchCode(new_value)

	def update_departmentCode(self):
		current_value = self.get_departmentCode()
		new_value = str(random.randint(10000000000, 99999999999))
		while current_value == new_value:
			new_value = str(random.randint(10, 99))
		self.set_departmentCode(new_value)

	def update_paymentCode(self):
		current_value = self.get_paymentCode()
		new_value = random.choice(['01', '02', '06', '16', None])
		while current_value == new_value:
			new_value = random.choice(['01', '02', '06', '16', 'CRED', None])
		self.set_paymentCode(new_value)

	def update_receiptDateToBank(self):
		current_value = self.get_receiptDateToBank()
		new_value = str(self.__faker__.date_between(start_date = '-1d', end_date = 'now'))
		while current_value == new_value:
			new_value = str(self.__faker__.date_between(start_date = '-1d', end_date = 'now'))
		self.set_receiptDateToBank(new_value)

	def update_date(self):
		current_value = self.get_date()
		new_value = str(self.__faker__.date_between(start_date = '-1d', end_date = 'now'))
		while current_value == new_value:
			new_value = str(self.__faker__.date_between(start_date = '-1d', end_date = 'now'))
		self.set_date(new_value)

	def update_amountNational(self):
		current_value = self.get_amountNational()
		new_value = round((random.random() * random.randint(10, 10000000)), 2)
		while current_value == new_value:
			new_value = round((random.random() * random.randint(10, 10000000)), 2)
		self.set_amountNational(new_value)

	def update_documentAmount(self):
		current_value = self.get_documentAmount()
		new_value = round((random.random() * random.randint(10, 10000000)), 2)
		while current_value == new_value:
			new_value = round((random.random() * random.randint(10, 10000000)), 2)
		self.set_documentAmount(new_value)

	def update_documentCurrency(self):
		current_value = self.get_documentCurrency()
		new_value = random.choice(list(config.dict_currency.keys()))
		while current_value == new_value:
			new_value = random.choice(list(config.dict_currency.keys()))
		self.set_documentCurrency(new_value)

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

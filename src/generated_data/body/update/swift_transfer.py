import random

from faker import Faker

from config import config
from src.generated_data.body.abstract.swift_transfer import SwiftTransferAbstract


class SwiftTransferUpdate(SwiftTransferAbstract):
	def __init__(
			self,
			counter_account: str,
			counter_name: str,
			counter_inn: str,
			counter_bank_name: str,
			counter_bank_swift: str,
			counter_bic: str,
			operation_purpose: str,
			document_date: str,
			document_number: str
	):
		super().__init__(
			counter_account = counter_account,
			counter_name = counter_name,
			counter_inn = counter_inn,
			counter_bank_name = counter_bank_name,
			counter_bank_swift = counter_bank_swift,
			counter_bic = counter_bic,
			operation_purpose = operation_purpose,
			document_number = document_number,
			document_date = document_date
		)

	def update_orderingCustomerAccount(self):
		current_account = self.get_orderingCustomerAccount()
		current_account_length = len(current_account)
		start_account_list = None
		residence_mask_length = 5
		while start_account_list is None:
			first_part_current_account = int(current_account[:residence_mask_length])
			if first_part_current_account in config.account_resident_masks:
				start_account_list = config.account_resident_masks
			if first_part_current_account in config.account_not_resident_masks:
				start_account_list = config.account_not_resident_masks
			residence_mask_length -= 1
			if residence_mask_length == 0:
				break

		start_account_value = str(
			start_account_list[
				random.randint(0, len(start_account_list) - 1)
			]
		)

		if len(start_account_value) != 5:
			for item in range(0, 4):
				start_account_value += str(item)
				if len(start_account_value) == 5:
					break

		currency_code = current_account[5:8]

		third_part_account = str(random.randint(10000, 19999))

		transit_value = current_account[13:15]

		last_part_account = ''
		for item in range(0, current_account_length - 15):
			last_part_account += str(random.randint(0, 9))

		self.set_orderingCustomerAccount(
			start_account_value +
			currency_code +
			third_part_account +
			transit_value +
			last_part_account
		)

	def update_orderingCustomerName(self, is_client: bool = False):
		if is_client:
			self.set_orderingCustomerName(
				random.choice(config.list_legal_forms) +
				' ' +
				'"' +
				random.choice(config.list_legal_names) +
				'"'
			)
		else:
			self.set_orderingCustomerName(
				random.choice(config.list_legal_forms) +
				' ' +
				'"' +
				random.choice(config.list_legal_names) +
				' КОНТРАГЕНТ"'
			)

	def update_orderingInstitutionOption(self):
		self.set_orderingInstitutionOption(
			random.choice(['A', 'B'])
		)

	def update_orderingInstitutionSWIFT(self):
		faker = Faker()
		self.set_orderingInstitutionSWIFT(faker.swift())

	def update_remittanceInformation(self, voCode: str = None):
		current_value = self.get_remittanceInformation()
		faker = Faker()
		new_value = ''
		if voCode:
			new_value += random.choice(
				[
					'{VO%s} ' % voCode,
					'{V0%s} ' % voCode,
					'(VO%s) ' % voCode,
					'(V0%s) ' % voCode,
				]
			)

		if current_value.__contains__('Операция по реестру'):
			new_value += 'Операция по реестру № ' + str(random.randint(10000, 99999))
			new_value += ' от ' + str(faker.date_between(start_date = '-10y', end_date = 'now'))
			new_value += ' в соответствии с Договором ' + str(random.randint(100000000, 9999999999))
			new_value += ' от ' + str(faker.date_between(start_date = '-5d', end_date = 'now'))
		else:
			new_value += 'Оплата по договору № ' + str(random.randint(10000, 99999))
			new_value += ' от ' + str(faker.date_between(start_date = '-10y', end_date = 'now'))
			new_value += ' за товар или услугу. МБ с НДС мб без'

		self.set_remittanceInformation(new_value)

	def get_orderingCustomerAccount(self):
		return self.orderingCustomerAccount

	def set_orderingCustomerAccount(self, value):
		self.orderingCustomerAccount = value

	def get_orderingCustomerName(self):
		return self.orderingCustomerName

	def set_orderingCustomerName(self, value):
		self.orderingCustomerName = value

	def get_orderingCustomerINN(self):
		return self.orderingCustomerINN

	def set_orderingCustomerINN(self, value):
		self.orderingCustomerINN = value

	def get_orderingInstitutionName(self):
		return self.orderingInstitutionName

	def set_orderingInstitutionName(self, value):
		self.orderingInstitutionName = value

	def get_orderingInstitutionSWIFT(self):
		return self.orderingInstitutionSWIFT

	def set_orderingInstitutionSWIFT(self, value):
		self.orderingInstitutionSWIFT = value

	def get_orderingInstitutionBIC(self):
		return self.orderingInstitutionBIC

	def set_orderingInstitutionBIC(self, value):
		self.orderingInstitutionBIC = value

	def get_orderingInstitutionOption(self):
		return self.orderingInstitutionOption

	def set_orderingInstitutionOption(self, value):
		self.orderingInstitutionOption = value

	def get_remittanceInformation(self):
		return self.remittanceInformation

	def set_remittanceInformation(self, value):
		self.remittanceInformation = value

	def get_docNumber(self):
		return self.docNumber

	def set_docNumber(self, value):
		self.docNumber = value

	def get_docDate(self):
		return self.docDate

	def set_docDate(self, value):
		self.docDate = value

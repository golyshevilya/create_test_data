import copy
import random

from src.generated_data.body.abstract.swift_transfer import SwiftTransferAbstract


class SwiftTransferCreate(SwiftTransferAbstract):
	def __init__(self,
	             counter_account: str,
	             counter_name: str,
	             counter_inn: str,
	             counter_bank_name: str,
	             counter_bank_swift: str,
	             counter_bic: str,
	             operation_purpose: str,
	             document_date: str,
	             document_number: str,
	             option: str):
		super().__init__(counter_account, counter_name, counter_inn, counter_bank_name, counter_bank_swift,
		                 counter_bic, operation_purpose, document_number, document_date, option)

	def __deepcopy__(self, memo):
		return SwiftTransferCreate(
			counter_account = copy.deepcopy(self.get_orderingCustomerAccount(), memo = memo),
			counter_name = copy.deepcopy(self.get_orderingCustomerName(), memo = memo),
			counter_inn = copy.deepcopy(self.get_orderingCustomerINN(), memo = memo),
			counter_bank_name = copy.deepcopy(self.get_orderingInstitutionName(), memo = memo),
			counter_bank_swift = copy.deepcopy(self.get_orderingInstitutionSWIFT(), memo = memo),
			counter_bic = copy.deepcopy(self.get_orderingInstitutionBIC(), memo = memo),
			operation_purpose = copy.deepcopy(self.get_remittanceInformation(), memo = memo),
			document_date = copy.deepcopy(self.get_docDate(), memo = memo),
			document_number = copy.deepcopy(self.get_docNumber(), memo = memo),
			option = copy.deepcopy(self.get_orderingInstitutionOption(), memo = memo)
		)

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

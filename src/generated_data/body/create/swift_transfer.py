import random

from src.generated_data.body.abstract.swift_transfer import SwiftTransferAbstract


class SwiftTransferCreate(SwiftTransferAbstract):
	def __init__(self, customer_account: str, customer_name: str, customer_inn: str, customer_bank_name: str,
	             customer_bank_swift: str, customer_bic: str, operation_purpose: str,
	             document_date: str, document_number: str):
		super().__init__(customer_account, customer_name, customer_inn, customer_bank_name, customer_bank_swift,
		                 customer_bic, operation_purpose, document_number, document_date)

		self.set_orderingInstitutionOption(random.choice(['A', 'B']))

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

import abc

class SwiftTransferAbstract(abc.ABC):

	def __init__(self,
	             customer_account: str,
	             customer_name: str,
	             customer_inn: str,
	             customer_bank_name: str,
	             customer_bank_swift: str,
	             customer_bic: str,
	             operation_purpose: str,
	             document_number: str,
	             document_date: str):
		self.orderingCustomerAccount: str = customer_account
		self.orderingCustomerName: str = customer_name
		self.orderingCustomerINN: str = customer_inn
		self.orderingInstitutionName: str = customer_bank_name
		self.orderingInstitutionSWIFT: str = customer_bank_swift
		self.orderingInstitutionBIC: str = customer_bic
		self.remittanceInformation: str = operation_purpose
		self.docNumber: str = document_number
		self.docDate: str = document_date
		self.orderingInstitutionOption = None

	def to_JSON(self):
		result_dict = {}
		for key, value in self.__dict__.items():
			if not key.startswith('__'):
				try:
					result_dict[key] = value.to_JSON
				except AttributeError:
					result_dict[key] = value
					continue
		return result_dict
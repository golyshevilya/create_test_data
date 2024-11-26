import abc


class SwiftTransferAbstract(abc.ABC):

	def __init__(
			self,
			counter_account: str,
			counter_name: str,
			counter_inn: str,
			counter_bank_name: str,
			counter_bank_swift: str,
			counter_bic: str,
			operation_purpose: str,
			document_number: str,
			document_date: str,
			option: str
	):
		self.orderingCustomerAccount: str = counter_account
		self.orderingCustomerName: str = counter_name
		self.orderingCustomerINN: str = counter_inn
		self.orderingInstitutionName: str = counter_bank_name
		self.orderingInstitutionSWIFT: str = counter_bank_swift
		self.orderingInstitutionBIC: str = counter_bic
		self.remittanceInformation: str = operation_purpose
		self.docNumber: str = document_number
		self.docDate: str = document_date
		self.orderingInstitutionOption = option

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

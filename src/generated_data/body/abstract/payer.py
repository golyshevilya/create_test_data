import abc


class PayerAbstract(abc.ABC):
	def __init__(self,
	             name: str,
	             account: str,
	             amount: str,
	             inn: str,
	             kpp: str,
	             bank_bic: str,
	             bank_name: str
	             ):
		self.name: str = name
		self.account: str = account
		self.amount: float = amount
		self.inn: str = inn
		self.kpp: str = kpp
		self.bankBIC: str = bank_bic
		self.bankName: str = bank_name

	def to_JSON(self):
		result_dict = {}
		for key, value in self.__dict__.items():
			if not key.startswith('__') and not callable(key):
				try:
					result_dict[key] = value.to_JSON
				except AttributeError:
					result_dict[key] = value
					continue
		return result_dict

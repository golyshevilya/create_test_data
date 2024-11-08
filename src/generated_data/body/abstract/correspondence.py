import abc
import copy


class CorrespondenceAbstract(abc.ABC):
	def __init__(self,
	             date: str,
	             amount: str,
	             account: str,
	             is_correspondence: bool = False,
	             account_currency: str = None):
		self.__is_correspondence__ = is_correspondence
		self.accountDate: str = date
		self.accountAmount: str = amount
		self.debitAccount: str = account
		self.accountCurrency = account_currency

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

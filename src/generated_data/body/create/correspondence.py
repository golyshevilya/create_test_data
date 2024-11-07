from config import config
from src.generated_data.body.abstract.correspondence import CorrespondenceAbstract


class CorrespondenceCreate(CorrespondenceAbstract):
	def __init__(self, date: str, amount: str, currency: str, account: str, is_correspondence: bool = False):

		super().__init__(date, amount, account, is_correspondence)
		self.set_accountCurrency(self.create_currency(currency_code = currency))

	@staticmethod
	def create_currency(currency_code: str):
		for key, value in config.dict_currency.items():
			if value == currency_code:
				return key

	def get_accountDate(self):
		return self.accountDate

	def set_accountDate(self, value):
		self.accountDate = value

	def get_accountAmount(self):
		return self.accountAmount

	def set_accountAmount(self, value):
		self.accountAmount = value

	def get_accountCurrency(self):
		return self.accountCurrency

	def set_accountCurrency(self, value):
		self.accountCurrency = value

	def get_debitAccount(self):
		return self.debitAccount

	def set_debitAccount(self, value):
		self.debitAccount = value

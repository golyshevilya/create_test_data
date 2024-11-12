import copy

from src.generated_data.body.abstract.payee import PayeeAbstract


class PayeeCreate(PayeeAbstract):
	def __init__(self, name: str, account: str, amount: str, account_digital_currency_code: str,
	             account_currency_code: str, inn: str, kpp: str, bank_bic: str, bank_name: str):
		super().__init__(name, account, amount, account_digital_currency_code, account_currency_code, inn, kpp,
		                 bank_bic, bank_name)

	def __deepcopy__(self, memo):
		return PayeeCreate(
			name=copy.deepcopy(self.get_name()),
			account=copy.deepcopy(self.get_account()),
			amount=copy.deepcopy(self.get_amount()),
			account_digital_currency_code = copy.deepcopy(self.get_accountDigitalCurrencyCode()),
			account_currency_code = copy.deepcopy(self.get_accountCurrencyCode()),
			inn=copy.deepcopy(self.get_inn()),
			kpp=copy.deepcopy(self.get_kpp()),
			bank_bic = copy.deepcopy(self.get_bankBIC()),
			bank_name = copy.deepcopy(self.get_bankName())
		)

	def get_name(self):
		return self.name

	def set_name(self, value):
		self.name = value

	def get_account(self):
		return self.account

	def set_account(self, value):
		self.account = value

	def get_amount(self):
		return self.amount

	def set_amount(self, value):
		self.amount = value

	def get_accountDigitalCurrencyCode(self):
		return self.accountDigitalCurrencyCode

	def set_accountDigitalCurrencyCode(self, value):
		self.accountDigitalCurrencyCode = value

	def get_accountCurrencyCode(self):
		return self.accountCurrencyCode

	def set_accountCurrencyCode(self, value):
		self.accountCurrencyCode = value

	def get_inn(self):
		return self.inn

	def set_inn(self, value):
		self.inn = value

	def get_kpp(self):
		return self.kpp

	def set_kpp(self, value):
		self.kpp = value

	def get_bankBIC(self):
		return self.bankBIC

	def set_bankBIC(self, value):
		self.bankBIC = value

	def get_bankName(self):
		return self.bankName

	def set_bankName(self, value):
		self.bankName = value

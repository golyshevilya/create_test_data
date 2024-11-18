import copy

from src.generated_data.body.abstract.payer import PayerAbstract


class PayerCreate(PayerAbstract):
	def __init__(self, name: str, account: str, amount: str, inn: str, kpp: str, bank_bic: str, bank_name: str):
		super().__init__(name, account, amount, inn, kpp, bank_bic, bank_name)

	def __deepcopy__(self, memo):
		return PayerCreate(
			name = copy.deepcopy(self.get_name(), memo = memo),
			account = copy.deepcopy(self.get_account(), memo = memo),
			amount = copy.deepcopy(self.get_amount(), memo = memo),
			inn = copy.deepcopy(self.get_inn(), memo = memo),
			kpp = copy.deepcopy(self.get_kpp(), memo = memo),
			bank_bic = copy.deepcopy(self.get_bankBIC(), memo = memo),
			bank_name = copy.deepcopy(self.get_bankName(), memo = memo)
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

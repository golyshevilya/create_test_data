import random
from typing import List

from config import config
from src.generated_data.body.abstract.payer import PayerAbstract


class PayerUpdate(PayerAbstract):
	def __init__(
			self,
			name: str,
			account: str,
			amount: str,
			inn: str,
			kpp: str,
			bank_bic: str,
			bank_name: str
	):
		super().__init__(
			name = name,
			account = account,
			amount = amount,
			inn = inn,
			kpp = kpp,
			bank_bic = bank_bic,
			bank_name = bank_name
		)

	def update_name(self, is_client: bool = False):
		if is_client:
			self.set_name(
				random.choice(config.list_legal_forms) +
				' ' +
				'"' +
				random.choice(config.list_legal_names) +
				'"'
			)
		else:
			self.set_name(
				random.choice(config.list_legal_forms) +
				' ' +
				'"' +
				random.choice(config.list_legal_names) +
				' КОНТРАГЕНТ"'
			)

	def update_account(self):
		current_account = self.get_account()
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

		self.set_account(
			start_account_value +
			currency_code +
			third_part_account +
			transit_value +
			last_part_account
		)

	@staticmethod
	def inn_ctrl_summ(nums: List, type: str):
		"""
		Подсчет контрольной суммы
		"""
		inn_ctrl_type = {
			'n2_12': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
			'n1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
			'n1_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
		}
		n = 0
		l = inn_ctrl_type[type]
		for i in range(0, len(l)):
			n += nums[i] * l[i]
		return n % 11 % 10

	def update_inn(self, length_inn: int = None):
		if not length_inn:
			length_inn = list((10, 12))[random.randint(0, 1)]
			if length_inn not in (10, 12):
				return None
			nums = [
				random.randint(1, 9) if x == 0
				else random.randint(0, 9)
				for x in range(0, 9 if length_inn == 10 else 10)
			]
			if length_inn == 12:
				n2 = self.inn_ctrl_summ(nums, 'n2_12')
				nums.append(n2)
				n1 = self.inn_ctrl_summ(nums, 'n1_12')
				nums.append(n1)
			elif length_inn == 10:
				n1 = self.inn_ctrl_summ(nums, 'n1_10')
				nums.append(n1)
			self.set_inn(''.join([str(x) for x in nums]))

	def update_bankBIC(self):
		self.set_bankBIC(
			random.randint(100000000, 999999999)
		)

	def update_kpp(self):
		self.set_kpp(
			str(random.randint(100000000, 999999999))
		)

	def update_bankName(self):
		self.set_bankName(
			random.choice(config.bank_names)
		)

	def update_amount(self, amount: str):
		self.set_amount(
			value = amount
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

import abc
import json
import random
from typing import List
import faker


class BodyAbstract(abc.ABC):

	def __init__(self, **kwargs):

		self.objectVersions = None
		self.correspondence = None
		self.payee = None
		self.payer = None
		self.operation = None
		self.swiftTransfer = None
		self.__faker__ = faker.Faker()

	def to_JSON(self):
		result_dict = {}
		for key, value in self.__dict__.items():
			if not key.startswith('__') and not callable(key):
				try:
					result_dict[key] = value.to_JSON()
				except AttributeError:
					result_dict[key] = value
					continue
		print(result_dict)
		return json.dumps(
			result_dict,
			sort_keys = False,
			indent = 4,
			ensure_ascii = False)

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

	def create_inn(self, length_inn: int = None):
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
			return ''.join([str(x) for x in nums])

import copy
import itertools
import random

from config import config
from src.generated_data.body.abstract.body import BodyAbstract


class BodyUpdate(BodyAbstract):

	def __init__(self, **kwargs):

		super().__init__(**kwargs)
		# kwargs = kwargs['kwargs']
		self.set_payee(copy.deepcopy(kwargs['payee']))
		self.set_payer(copy.deepcopy(kwargs['payer']))
		self.set_operation(copy.deepcopy(kwargs['operation']))
		self.set_objectVersions(copy.deepcopy(kwargs['objectVersions']))
		self.set_swiftTransfer(copy.deepcopy(kwargs['swiftTransfer']))

	@staticmethod
	def create_correspondence(is_correspondence_account: str):
		if is_correspondence_account == 'рандом':
			return True if random.randint(0, 1) == 1 else False
		elif is_correspondence_account == 'да':
			return True
		else:
			return False

	@staticmethod
	def create_account_currency(account):
		for key, value in config.dict_currency.items():
			if value == account[5:8]:
				return key, value
		return None, None

	@staticmethod
	def create_document_currency(operation_currency):
		if operation_currency == 'рандом':
			key = random.choice(list(config.dict_currency.keys()))
			return key, config.dict_currency[key]
		elif operation_currency == 'рубли':
			key = random.choice(['RUB', 'RUR'])
			return key, config.dict_currency[key]
		else:
			key = random.choice(itertools.islice(config.dict_currency.values(), len(config.dict_currency) - 2))
			return key, config.dict_currency[key]

	@staticmethod
	def create_is_registry(is_registry: str):
		if is_registry == 'рандом':
			return True if random.randint(0, 1) == 0 else False
		elif is_registry == 'да':
			return True
		else:
			return False

	@staticmethod
	def create_currency_operation_code(currency_operation_code: str):
		if currency_operation_code == 'рандом':
			return str(random.randint(10000, 99999))
		else:
			return currency_operation_code

	def create_purpose(self, is_vo_code: bool = False, is_registry: bool = False):
		result = ''
		if is_vo_code:
			result += random.choice(
				[
					'{VO%s} ' % self.__currency_operation_code__,
					'{V0%s} ' % self.__currency_operation_code__,
					'(VO%s) ' % self.__currency_operation_code__,
					'(V0%s) ' % self.__currency_operation_code__,
				]
			)

		if is_registry:
			result += 'Операция по реестру № ' + str(random.randint(10000, 99999))
			result += ' от ' + str(self.__faker__.date_between(start_date = '-10y', end_date = 'now'))
			result += ' в соответствии с Договором ' + str(random.randint(100000000, 9999999999))
			result += ' от ' + str(self.__faker__.date_between(start_date = '-5d', end_date = 'now'))
		else:
			result += 'Оплата по договору № ' + str(random.randint(10000, 99999))
			result += ' от ' + str(self.__faker__.date_between(start_date = '-10y', end_date = 'now'))
			result += ' за товар или услугу. МБ с НДС мб без'

		return result

	@staticmethod
	def create_person_name(is_client: bool = False):
		if is_client:
			return random.choice(config.list_legal_forms) + ' ' + '"' + random.choice(config.list_legal_names) + '"'
		else:
			return random.choice(config.list_legal_forms) + ' ' + '"' + random.choice(
				config.list_legal_names) + ' КОНТРАГЕНТ"'

	@staticmethod
	def create_customer_currency(customer_currency: str):
		if customer_currency == 'рандом':
			return random.choice(list(config.dict_currency.values()))
		elif customer_currency == 'рубли':
			return '810'
		else:
			return random.choice(itertools.islice(config.dict_currency.values(), len(config.dict_currency) - 2))

	@staticmethod
	def create_is_transit(is_transit: str):
		if is_transit == 'рандом':
			return True if random.randint(0, 1) == 0 else False
		elif is_transit == 'резидент':
			return True
		else:
			return False

	@staticmethod
	def create_is_resident(customer: str):
		if customer == 'рандом':
			return True if random.randint(0, 1) == 0 else False
		elif customer == 'резидент':
			return True
		else:
			return False

	@staticmethod
	def create_account(is_resident: bool = True,
	                   is_transit: bool = False,
	                   account_length: int = 20,
	                   currency_code: str = '810',
	                   is_client_account: bool = True,
	                   is_correspondence_account: bool = False
	                   ):
		if is_correspondence_account:
			start_account_list = config.account_correspondence
		else:
			if is_resident:
				start_account_list = config.account_resident_masks
			else:
				start_account_list = config.account_not_resident_masks
		start_account_value = str(start_account_list[random.randint(0, len(start_account_list) - 1)])

		if len(start_account_value) != 5:
			for item in range(0, 4):
				start_account_value += str(item)
				if len(start_account_value) == 5:
					break

		if currency_code in config.dict_currency.keys():
			currency_code = config.dict_currency[currency_code]

		third_part_account = str(random.randint(10000, 19999))

		transit_value = '00'
		if is_transit:
			transit_value = '10' if random.randint(0, 1) == 0 else '02'

		last_part_account = ''
		if is_client_account:
			account_length = 20
		for item in range(0, account_length - 15):
			last_part_account += str(random.randint(0, 9))

		return start_account_value + currency_code + third_part_account + transit_value + last_part_account

	def get_swiftTransfer(self):
		return self.swiftTransfer

	def set_swiftTransfer(self, value):
		self.swiftTransfer = value

	def get_operation(self):
		return self.operation

	def set_operation(self, value):
		self.operation = value

	def get_payer(self):
		return self.payer

	def set_payer(self, value):
		self.payer = value

	def get_payee(self):
		return self.payee

	def set_payee(self, value):
		self.payee = value

	def get_correspondence(self):
		return self.correspondence

	def set_correspondence(self, value):
		self.correspondence = value

	def get_objectVersions(self):
		return self.objectVersions

	def set_objectVersions(self, value):
		self.objectVersions = value

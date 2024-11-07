from src.generated_data.body.abstract.object_versions import ObjectVersionAbstract
from src.generated_data.body.create.turn import TurnCreate
from src.generated_data.body.create.doc_data import DocDataCreate
from src.generated_data.body.create.mt_currency import MTCurrency
import random


class ObjectVersionsCreate(ObjectVersionAbstract):
	def __init__(self, is_versions_similar: bool = False, action_doc_data: str = 'insert', action_turn: str = 'insert',
	             action_mt_currency: str = 'insert'):

		super().__init__()
		self.__version_doc_data__, self.__version__turn__, self.__version__mt_currency__ = self.create_versions(
			is_versions_similar = is_versions_similar)

		self.set_turn_id(
			'shard%s:%s' % (
				random.randint(0, 5),
				random.randint(1000000000000000000, 9999999999999999999)
			)
		)
		self.set_docData(
			DocDataCreate(
				action = action_doc_data[:1].upper(),
				version = self.__version_doc_data__
			)
		)
		self.set_turn(
			TurnCreate(
				action = action_turn[:1].upper(),
				version = self.__version__turn__
			)
		)
		self.set_mtCurrency(
			MTCurrency(
				action = action_mt_currency[:1].upper(),
				version = self.__version__mt_currency__
			)
		)

	@staticmethod
	def create_versions(is_versions_similar: bool):
		if is_versions_similar:
			version = random.randint(1000000000000, 9999999999999)
			return version, version, version
		else:
			return random.randint(1000000000000, 9999999999999), random.randint(1000000000000,
			                                                                    9999999999999), random.randint(
				1000000000000, 9999999999999)

	def get_docData(self):
		return self.docData

	def set_docData(self, value):
		self.docData = value

	def get_turn(self):
		return self.turn

	def set_turn(self, value):
		self.turn = value

	def get_mtCurrency(self):
		return self.mtCurrency

	def set_mtCurrency(self, value):
		self.mtCurrency = value

	def get_turn_id(self):
		return self.turn_id

	def set_turn_id(self, value):
		self.turn_id = value

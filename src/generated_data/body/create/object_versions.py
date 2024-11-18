import copy

from src.generated_data.body.abstract.object_versions import ObjectVersionAbstract
from src.generated_data.body.create.turn import TurnCreate
from src.generated_data.body.create.doc_data import DocDataCreate
from src.generated_data.body.create.mt_currency import MTCurrency
import random


class ObjectVersionsCreate(ObjectVersionAbstract):
	def __init__(self,
	             turn_id: str,
	             version_doc_data: str,
	             version_turn: str,
	             version_mt_currency: str,
	             action_doc_data: str = 'insert',
	             action_turn: str = 'insert',
	             action_mt_currency: str = 'insert'):
		super().__init__(turn_id = turn_id)

		self.set_docData(
			DocDataCreate(
				action = action_doc_data[:1].upper(),
				version = version_doc_data
			)
		)
		self.set_turn(
			TurnCreate(
				action = action_turn[:1].upper(),
				version = version_turn
			)
		)
		self.set_mtCurrency(
			MTCurrency(
				action = action_mt_currency[:1].upper(),
				version = version_mt_currency
			)
		)

	def __deepcopy__(self, memo):
		return ObjectVersionsCreate(
			turn_id = copy.deepcopy(self.get_turn_id(), memo = memo),
			version_doc_data = copy.deepcopy(self.get_docData().get_version(), memo = memo),
			version_turn = copy.deepcopy(self.get_turn().get_version(), memo = memo),
			version_mt_currency = copy.deepcopy(self.get_mtCurrency().get_version(), memo = memo),
			action_doc_data = copy.deepcopy(self.get_docData().get_action(), memo = memo),
			action_turn = copy.deepcopy(self.get_turn().get_action(), memo = memo),
			action_mt_currency = copy.deepcopy(self.get_mtCurrency().get_action(), memo = memo)
		)

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

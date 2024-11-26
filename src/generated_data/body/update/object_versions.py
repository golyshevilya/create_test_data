from src.generated_data.body.abstract.object_versions import ObjectVersionAbstract
from src.generated_data.body.create.turn import TurnCreate
from src.generated_data.body.create.doc_data import DocDataCreate
from src.generated_data.body.create.mt_currency import MTCurrency
import random


class ObjectVersionsUpdate(ObjectVersionAbstract):
	def __init__(self, turn_id: str):

		super().__init__()

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

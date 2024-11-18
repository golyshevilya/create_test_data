import abc

class ObjectVersionAbstract(abc.ABC):

	def __init__(self, turn_id: str):
		self.mtCurrency = None
		self.turn = None
		self.docData = None
		self.turn_id = turn_id

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
import abc

class VersionAbstract(abc.ABC):
	def __init__(self, action: str, version: str):
		self.action: str = action
		self.version: int = version

	@property
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

	def get_action(self):
		return self.action

	def set_action(self, value):
		self.action = value

	def get_version(self):
		return self.version

	def set_version(self, value):
		self.version = value

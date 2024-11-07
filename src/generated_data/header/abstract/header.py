import abc
import json


class HeaderAbstract(abc.ABC):

	def __init__(self):
		self.registerId: str = None
		self.divisionId: str = None
		self.srcModule: str = None
		self.evtId: str = None
		self.sndDate: str = None
		self.epkId: str = None
		self.requestId: str = None
		self.sendServiceId: str = None
		self.docGuid: str = None
		self.kindDoc: str = None
		self.accountType: str = None
		self.sourceData: str = None
		self.creatorSystem: str = None

	def to_JSON(self):
		return json.dumps(
			self,
			default = lambda o: o.__dict__,
			sort_keys = True,
			indent = 4)

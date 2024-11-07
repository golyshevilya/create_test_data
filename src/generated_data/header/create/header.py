import uuid
import datetime
import random
import json

from config import config
from src.generated_data.header.abstract.header import HeaderAbstract


class HeaderCreate(HeaderAbstract):
	def __init__(self, direction: str, division_id: str = None, epk_id: str = None,
	             is_transit_customer_account: str = None, is_registry: str = None) -> object:
		super().__init__()
		self.set_registerId(random.randint(1000000000000000000, 9999999999999999999))
		self.set_divisionId(str(division_id if division_id else random.randint(10000000000, 99999999999)))
		self.set_srcModule('crediting-payment')
		self.set_evtId(self.create_uuid(type = 'evtId'))
		self.set_sndDate(datetime.datetime.today().strftime('%Y-%m-%dT%H:%M:%S'))
		self.set_epkId(epk_id if epk_id else str(random.randint(1000000000000000000, 9999999999999999999)))
		self.set_requestId(self.create_uuid(type = 'requestId'))
		self.set_sendServiceId(self.create_uuid(type = 'sendServiceId'))
		self.set_docGuid(self.create_uuid(type = 'docGuid'))
		self.set_kindDoc(random.choice(['01', '02', '06', '16', 'CRED', None]))
		self.set_accountType(
			self.create_transition_account(is_transit_customer_account = is_transit_customer_account))
		self.set_creatorSystem(self.create_creator_system(direction = direction, is_registry = is_registry))

	@staticmethod
	def create_transition_account(is_transit_customer_account: str) -> str:
		if is_transit_customer_account == 'рандом':
			return 'LegalSettlementTransitAccountRegisterType' if random.randint(0,
			                                                                     1) == 0 else 'LegalSettlementCheckingAccountRegisterType'
		else:
			if is_transit_customer_account == 'да':
				return 'LegalSettlementTransitAccountRegisterType'
			else:
				return 'LegalSettlementCheckingAccountRegisterType'

	@staticmethod
	def create_creator_system(direction: str, is_registry: str):
		if direction == 'зачисление':
			return 'urn:subsystems:99-ppr:cred-' + random.choice(config.creator_system_for_enrollment)
		else:
			if direction == 'списание':
				if is_registry == 'рандом':
					return 'urn:subsystems:99-pprb:legal-payment-cloud' if random.randint(0, 1) == 0 else random.choice(
						config.creator_system_for_extract)
				else:
					if is_registry == 'да':
						return 'urn:subsystems:99-pprb:legal-payment-cloud'
					else:
						return random.choice(config.creator_system_for_extract)

	@staticmethod
	def create_uuid(type: str):
		if type in ['requestId', 'sendServiceId']:
			return str('BDVO_GEN_' + str(uuid.uuid4()))
		if type in ['docGuid', 'evtId']:
			return str(uuid.uuid4())

	def get_registerId(self):
		return self.registerId

	def set_registerId(self, value):
		self.registerId = value

	def get_divisionId(self):
		return self.divisionId

	def set_divisionId(self, value):
		self.divisionId = value

	def get_srcModule(self):
		return self.srcModule

	def set_srcModule(self, value):
		self.srcModule = value

	def get_evtId(self):
		return self.evtId

	def set_evtId(self, value):
		self.evtId = value

	def get_sndDate(self):
		return self.sndDate

	def set_sndDate(self, value):
		self.sndDate = value

	def get_epkId(self):
		return self.epkId

	def set_epkId(self, value):
		self.epkId = value

	def get_requestId(self):
		return self.requestId

	def set_requestId(self, value):
		self.requestId = value

	def get_sendServiceId(self):
		return self.sendServiceId

	def set_sendServiceId(self, value):
		self.sendServiceId = value

	def get_docGuid(self):
		return self.docGuid

	def set_docGuid(self, value):
		self.docGuid = value

	def get_kindDoc(self):
		return self.kindDoc

	def set_kindDoc(self, value):
		self.kindDoc = value

	def get_accountType(self):
		return self.accountType

	def set_accountType(self, value):
		self.accountType = value

	def get_sourceData(self):
		return self.sourceData

	def set_sourceData(self, value):
		self.sourceData = value

	def get_creatorSystem(self):
		return self.creatorSystem

	def set_creatorSystem(self, value):
		self.creatorSystem = value

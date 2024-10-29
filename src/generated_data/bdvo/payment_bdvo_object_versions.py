from src.generated_data.bdvo.payemnt_bdvo_turn import Turn
from src.generated_data.bdvo.payment_bdvo_doc_data import DocData
from src.generated_data.bdvo.payment_bdvo_mt_currency import MTCurrency
import random

class ObjectVersions:
    def __init__(self, sender_system: str, is_versions_similar: bool = False, action_doc_data: str = 'insert', action_turn: str = 'insert', action_mt_currency: str = 'insert'):
        
        
        
        self.__sender_system__ = sender_system
        self.__version_doc_data__, self.__version__turn__, self.__version__mt_currency__ = self.create_versions(is_versions_similar=is_versions_similar)
        
        self.turnId = 'shard%s:%s'%(random.randint(0,5), random.randint(1000000000000000000, 9999999999999999999))
        self.docData: DocData = DocData(
            action=action_doc_data[:1],
            version=self.__version_doc_data__
        )
        self.turn: Turn = Turn(
            action=action_turn[:1],
            version=self.__version__turn__
        )
        self.mtCurrency: MTCurrency = MTCurrency(
            action=action_mt_currency[:1],
            version=self.__version__mt_currency__
        )
        
        

    def to_JSON(self):
        if self.__sender_system__ != 'выписка':
            return None
        result_dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith('__') and not callable(key):
                try:
                    result_dict[key] = value.to_JSON()
                except:
                    result_dict[key] = value
                    continue
        return result_dict
    
    def create_versions(self, is_versions_similar: bool):
        if is_versions_similar:
            version = random.randint(1000000000000, 9999999999999)
            return version, version, version
        else:
            return random.randint(1000000000000, 9999999999999), random.randint(1000000000000, 9999999999999), random.randint(1000000000000, 9999999999999)

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

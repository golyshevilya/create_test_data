from src.generated_data.bdvo.payemnt_bdvo_turn import Turn
from src.generated_data.bdvo.payment_bdvo_doc_data import DocData
from src.generated_data.bdvo.payment_bdvo_mt_currency import MTCurrency


class ObjectVersions:
    def __init__(self):
        self.turn: str = None
        self.docData: DocData = DocData()
        self.turn: Turn = Turn()
        self.mtCurrency: MTCurrency = MTCurrency()

    def get_turn(self):
        return self.turn

    def set_turn(self, value):
        self.turn = value

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

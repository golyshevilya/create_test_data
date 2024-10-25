from src.enrollment.body.enrollment_account import Account
from src.enrollment.body.enrollment_turn import Turn
from src.enrollment.body.enrollment_doc_data import DocData

class Enrollment:
    def __init__(self, **kwargs):
        self.account = Account(**kwargs)
        self.turn = Turn(**kwargs)
        self.docData = DocData(**kwargs)

        


        
        

        
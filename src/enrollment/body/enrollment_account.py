class Account:
    def __init__(self, **kwargs):
        
        self.accNum: str = kwargs['customer_account']
        self.registerId: str = kwargs['customer_register_id']

    def get_accNum(self):
        return self.accNum

    def set_accNum(self, value: str):
        self.accNum = value

    def get_registerId(self):
        return self.registerId

    def set_registerId(self, value: str):
        self.registerId = value
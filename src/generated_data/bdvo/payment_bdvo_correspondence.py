class Correspondece:
    def __init__(self,
                 sender_system: str):
        self.__sender_system__: str = sender_system
        self.accountDate: str = None
        self.accountAmount: str = None
        self.accountCurrency: str = None
        self.debitAccount: str = None

    def to_JSON(self):
        if self.__sender_system__ == 'выписка':
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
    
    def get_accountDate(self):
        return self.accountDate

    def set_accountDate(self, value):
        self.accountDate = value

    def get_accountAmount(self):
        return self.accountAmount

    def set_accountAmount(self, value):
        self.accountAmount = value

    def get_accountCurrency(self):
        return self.accountCurrency

    def set_accountCurrency(self, value):
        self.accountCurrency = value

    def get_debitAccount(self):
        return self.debitAccount

    def set_debitAccount(self, value):
        self.debitAccount = value

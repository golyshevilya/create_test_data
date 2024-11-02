from config import config

class Correspondece:
    def __init__(self,
                 date: str,
                 amount: str,
                 currency: str,
                 account: str,
                 is_correspondence: bool = False):
        self.__is_correspondence__ = is_correspondence
        self.accountDate: str = date
        self.accountAmount: str = amount
        self.accountCurrency: str = self.create_currency(currency_code=currency)
        self.debitAccount: str = account

    def to_JSON(self):
        result_dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith('__') and not callable(key):
                try:
                    result_dict[key] = value.to_JSON()
                except:
                    result_dict[key] = value
                    continue
        return result_dict
    
    def create_currency(self, currency_code: str):
        for key, value in config.dict_currency.items():
            if value == currency_code:
                return key
    
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

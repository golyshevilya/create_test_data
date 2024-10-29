class Payee:
    def __init__(self,
                 name: str,
                 account: str,
                 amount: str, 
                 account_digital_curency_code: str,
                 account_currency_code: str,
                 inn: str,
                 kpp: str,
                 bank_bic: str,
                 bank_name: str
                ):
        self.name: str = name
        self.account: str = account
        self.amount: float = amount
        self.accountDigitalCurrencyCode: int = account_digital_curency_code
        self.accountCurrencyCode: str = account_currency_code
        self.inn: str = inn
        self.kpp: str = kpp
        self.bankBIC: str = bank_bic
        self.bankName: str = bank_name

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
    
    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_account(self):
        return self.account

    def set_account(self, value):
        self.account = value

    def get_amount(self):
        return self.amount

    def set_amount(self, value):
        self.amount = value

    def get_accountDigitalCurrencyCode(self):
        return self.accountDigitalCurrencyCode

    def set_accountDigitalCurrencyCode(self, value):
        self.accountDigitalCurrencyCode = value

    def get_accountCurrencyCode(self):
        return self.accountCurrencyCode

    def set_accountCurrencyCode(self, value):
        self.accountCurrencyCode = value

    def get_inn(self):
        return self.inn

    def set_inn(self, value):
        self.inn = value

    def get_kpp(self):
        return self.kpp

    def set_kpp(self, value):
        self.kpp = value

    def get_bankBIC(self):
        return self.bankBIC

    def set_bankBIC(self, value):
        self.bankBIC = value

    def get_bankName(self):
        return self.bankName

    def set_bankName(self, value):
        self.bankName = value

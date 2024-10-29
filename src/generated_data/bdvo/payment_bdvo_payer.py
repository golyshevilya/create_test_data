class Payer:
    def __init__(self,
                 name: str,
                 account: str,
                 amount: str,
                 inn: str,
                 kpp: str,
                 bank_bic: str,
                 bank_name: str
                ):
        self.name: str = name
        self.account: str = account
        self.amount: float = amount
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

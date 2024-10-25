class Correspondece:
    def __init__(self):
        self.accountDate: str = None
        self.accountAmount: str = None
        self.accountCurrency: str = None
        self.debitAccount: str = None

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

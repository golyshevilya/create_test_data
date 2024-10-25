class Turn:
    def __init__(self, **kwargs):
        self.date = kwargs['operation_date']
        self.astronomicalDate = kwargs['astronomical_date']
        self.amount = kwargs['operation_amount']
        self.nationalAmount = kwargs['operation_national_amount']

    def get_date(self):
        return self.date

    def set_date(self, value):
        self.date = value

    def get_astronomicalDate(self):
        return self.astronomicalDate

    def set_astronomicalDate(self, value):
        self.astronomicalDate = value

    def get_amount(self):
        return self.amount

    def set_amount(self, value):
        self.amount = value

    def get_nationalAmount(self):
        return self.nationalAmount

    def set_nationalAmount(self, value):
        self.nationalAmount = value

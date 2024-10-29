from config import config


class SwiftTransfer:
    def __init__(self, 
                 sender_system: str, 
                 customer_account: str, 
                 customer_name: str, 
                 customer_inn: str, 
                 customer_bank_name: str, 
                 customer_bank_swift: str,
                 customer_bic: str, 
                 operation_purpose: str,
                 documnet_number: str,
                 document_date: str):
        self.orderingCustomerAccount: str = customer_account
        self.orderingCustomerName: str = customer_name
        self.orderingCustomerINN: str = customer_inn if sender_system == 'зачисления' else None
        self.orderingInstitutionName: str = customer_bank_name
        self.orderingInstitutionSWIFT: str = customer_bank_swift 
        self.orderingInstitutionBIC: str = customer_bic if sender_system == 'зачисления' else None
        self.orderingInstitutionOption: str = None
        self.remittanceInformation: str = operation_purpose
        self.docNumber: str = documnet_number if sender_system == 'зачисления' else None
        self.docDate: str = document_date if sender_system == 'зачисления' else None

    def to_JSON(self):
        result_dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith('__'):
                try:
                    result_dict[key] = value.to_JSON()
                except:
                    result_dict[key] = value
                    continue
        return result_dict
    
    def get_orderingCustomerAccount(self):
        return self.orderingCustomerAccount

    def set_orderingCustomerAccount(self, value):
        self.orderingCustomerAccount = value

    def get_orderingCustomerName(self):
        return self.orderingCustomerName

    def set_orderingCustomerName(self, value):
        self.orderingCustomerName = value

    def get_orderingCustomerINN(self):
        return self.orderingCustomerINN

    def set_orderingCustomerINN(self, value):
        self.orderingCustomerINN = value

    def get_orderingInstitutionName(self):
        return self.orderingInstitutionName

    def set_orderingInstitutionName(self, value):
        self.orderingInstitutionName = value

    def get_orderingInstitutionSWIFT(self):
        return self.orderingInstitutionSWIFT

    def set_orderingInstitutionSWIFT(self, value):
        self.orderingInstitutionSWIFT = value

    def get_orderingInstitutionBIC(self):
        return self.orderingInstitutionBIC

    def set_orderingInstitutionBIC(self, value):
        self.orderingInstitutionBIC = value

    def get_orderingInstitutionOption(self):
        return self.orderingInstitutionOption

    def set_orderingInstitutionOption(self, value):
        self.orderingInstitutionOption = value

    def get_remittanceInformation(self):
        return self.remittanceInformation

    def set_remittanceInformation(self, value):
        self.remittanceInformation = value

    def get_docNumber(self):
        return self.docNumber

    def set_docNumber(self, value):
        self.docNumber = value

    def get_docDate(self):
        return self.docDate

    def set_docDate(self, value):
        self.docDate = value

class DocData:
    def __init__(self, **kwargs):
        self.requestId = kwargs['request_id']
        self.updUID = kwargs['document_id']
        self.sendServiceId = kwargs['service_id']
        self.systemId = kwargs['system_id']
        self.status = kwargs['document_status']
        self.docDate = kwargs['document_date']
        self.docNumber = kwargs['document_number']
        self.docAmount = kwargs['document_amount']
        self.docCurrencyCode = kwargs['document_currency_code']
        self.purpose = kwargs['operation_purpose']
        self.purposeCode = kwargs['purpose_code']
        self.payerName = kwargs['counter_name']
        self.payerAccount = kwargs['counter_account']
        self.payerAccountCurrencyCode = kwargs['counter_account_currency_code']
        self.payerInn = kwargs['counter_inn']
        self.payerKpp = kwargs['counter_kpp']
        self.payerBankBic = kwargs['counter_bank_bic']
        self.payerNameBank = kwargs['counter_name_bank']
        self.payerBankCorrAccount = kwargs['counter_bank_corr_account']
        self.payerAccountDigitalCurrencyCode = kwargs['counter_account_digital_currency_code']
        self.payeeAmount = kwargs['customer_amount']
        self.payeeAccountCurrencyCode = kwargs['customer_account_currency_code']
        self.payeeEpkId = kwargs['customer_epk_id']
        self.payeeRegisterId = kwargs['customer_register_id']
        self.payeeName = kwargs['customer_register_id']
        self.payeeAccount = kwargs['customer_account']
        self.payeeInn = kwargs['customer_inn']
        self.payeeKpp = kwargs['customer_kpp']
        self.payeeBankBic = kwargs['customer_bank_bic']
        self.payeeNameBank = kwargs['customer_name_bank']
        self.payeeBankCorrAccount = kwargs['customer_bank_corr_account']
        self.payeeAccountDigitalCurrencyCode = kwargs['customer_account_digital_currency_code']
        self.priority = kwargs['priority']
        self.transCurr = kwargs['customer_account_digital_currency_code']
        self.deliveryKind = kwargs['operation_type']
        self.payingCondition = kwargs['paying_condition']
        self.payingConditionDate = kwargs['paying_condition_date']
        self.voCode = kwargs['voCode']
        self.uip = kwargs['code_uin']
        self.drawerStatus101 = kwargs['drawer_status_101']
        self.kbk = kwargs['kbk']
        self.oktmo = kwargs['oktmo']
        self.reasonCode106 = kwargs['reason_code_106']
        self.taxPeriod107 = kwargs['tax_period_107']
        self.docNumber108 = kwargs['document_number_108']
        self.docDate109 = kwargs['document_date_109']
        self.paymentKind110 = kwargs['payment_kind_110']
        self.incomeTypeCode = kwargs['income_type_code']
        self.receiptDate = kwargs['receipt_date']
        self.filialCode = kwargs['terbank']
        self.divisionId = kwargs['department_code']
        self.increaseCorrespondentAccountDate = kwargs['in_corr_account_date']
        self.corAccountAmount = kwargs['corr_account_amount']
        self.corAccountCurrency = kwargs['corr_account_cyrrency']
        self.debitCorAccount = kwargs['debit_corr_account']

    def get_requestId(self):
        return self.requestId

    def set_requestId(self, value):
        self.requestId = value

    def get_updUID(self):
        return self.updUID

    def set_updUID(self, value):
        self.updUID = value

    def get_sendServiceId(self):
        return self.sendServiceId

    def set_sendServiceId(self, value):
        self.sendServiceId = value

    def get_systemId(self):
        return self.systemId

    def set_systemId(self, value):
        self.systemId = value

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_docDate(self):
        return self.docDate

    def set_docDate(self, value):
        self.docDate = value

    def get_docNumber(self):
        return self.docNumber

    def set_docNumber(self, value):
        self.docNumber = value

    def get_docAmount(self):
        return self.docAmount

    def set_docAmount(self, value):
        self.docAmount = value

    def get_docCurrencyCode(self):
        return self.docCurrencyCode

    def set_docCurrencyCode(self, value):
        self.docCurrencyCode = value

    def get_purpose(self):
        return self.purpose

    def set_purpose(self, value):
        self.purpose = value

    def get_purposeCode(self):
        return self.purposeCode

    def set_purposeCode(self, value):
        self.purposeCode = value

    def get_payerName(self):
        return self.payerName

    def set_payerName(self, value):
        self.payerName = value

    def get_payerAccount(self):
        return self.payerAccount

    def set_payerAccount(self, value):
        self.payerAccount = value

    def get_payerAccountCurrencyCode(self):
        return self.payerAccountCurrencyCode

    def set_payerAccountCurrencyCode(self, value):
        self.payerAccountCurrencyCode = value

    def get_payerInn(self):
        return self.payerInn

    def set_payerInn(self, value):
        self.payerInn = value

    def get_payerKpp(self):
        return self.payerKpp

    def set_payerKpp(self, value):
        self.payerKpp = value

    def get_payerBankBic(self):
        return self.payerBankBic

    def set_payerBankBic(self, value):
        self.payerBankBic = value

    def get_payerNameBank(self):
        return self.payerNameBank

    def set_payerNameBank(self, value):
        self.payerNameBank = value

    def get_payerBankCorrAccount(self):
        return self.payerBankCorrAccount

    def set_payerBankCorrAccount(self, value):
        self.payerBankCorrAccount = value

    def get_payerAccountDigitalCurrencyCode(self):
        return self.payerAccountDigitalCurrencyCode

    def set_payerAccountDigitalCurrencyCode(self, value):
        self.payerAccountDigitalCurrencyCode = value

    def get_payeeAmount(self):
        return self.payeeAmount

    def set_payeeAmount(self, value):
        self.payeeAmount = value

    def get_payeeAccountCurrencyCode(self):
        return self.payeeAccountCurrencyCode

    def set_payeeAccountCurrencyCode(self, value):
        self.payeeAccountCurrencyCode = value

    def get_payeeEpkId(self):
        return self.payeeEpkId

    def set_payeeEpkId(self, value):
        self.payeeEpkId = value

    def get_payeeRegisterId(self):
        return self.payeeRegisterId

    def set_payeeRegisterId(self, value):
        self.payeeRegisterId = value

    def get_payeeName(self):
        return self.payeeName

    def set_payeeName(self, value):
        self.payeeName = value

    def get_payeeAccount(self):
        return self.payeeAccount

    def set_payeeAccount(self, value):
        self.payeeAccount = value

    def get_payeeInn(self):
        return self.payeeInn

    def set_payeeInn(self, value):
        self.payeeInn = value

    def get_payeeKpp(self):
        return self.payeeKpp

    def set_payeeKpp(self, value):
        self.payeeKpp = value

    def get_payeeBankBic(self):
        return self.payeeBankBic

    def set_payeeBankBic(self, value):
        self.payeeBankBic = value

    def get_payeeNameBank(self):
        return self.payeeNameBank

    def set_payeeNameBank(self, value):
        self.payeeNameBank = value

    def get_payeeBankCorrAccount(self):
        return self.payeeBankCorrAccount

    def set_payeeBankCorrAccount(self, value):
        self.payeeBankCorrAccount = value

    def get_payeeAccountDigitalCurrencyCode(self):
        return self.payeeAccountDigitalCurrencyCode

    def set_payeeAccountDigitalCurrencyCode(self, value):
        self.payeeAccountDigitalCurrencyCode = value

    def get_priority(self):
        return self.priority

    def set_priority(self, value):
        self.priority = value

    def get_transCurr(self):
        return self.transCurr

    def set_transCurr(self, value):
        self.transCurr = value

    def get_deliveryKind(self):
        return self.deliveryKind

    def set_deliveryKind(self, value):
        self.deliveryKind = value

    def get_payingCondition(self):
        return self.payingCondition

    def set_payingCondition(self, value):
        self.payingCondition = value

    def get_payingConditionDate(self):
        return self.payingConditionDate

    def set_payingConditionDate(self, value):
        self.payingConditionDate = value

    def get_voCode(self):
        return self.voCode

    def set_voCode(self, value):
        self.voCode = value

    def get_uip(self):
        return self.uip

    def set_uip(self, value):
        self.uip = value

    def get_drawerStatus101(self):
        return self.drawerStatus101

    def set_drawerStatus101(self, value):
        self.drawerStatus101 = value

    def get_kbk(self):
        return self.kbk

    def set_kbk(self, value):
        self.kbk = value

    def get_oktmo(self):
        return self.oktmo

    def set_oktmo(self, value):
        self.oktmo = value

    def get_reasonCode106(self):
        return self.reasonCode106

    def set_reasonCode106(self, value):
        self.reasonCode106 = value

    def get_taxPeriod107(self):
        return self.taxPeriod107

    def set_taxPeriod107(self, value):
        self.taxPeriod107 = value

    def get_docNumber108(self):
        return self.docNumber108

    def set_docNumber108(self, value):
        self.docNumber108 = value

    def get_docDate109(self):
        return self.docDate109

    def set_docDate109(self, value):
        self.docDate109 = value

    def get_paymentKind110(self):
        return self.paymentKind110

    def set_paymentKind110(self, value):
        self.paymentKind110 = value

    def get_incomeTypeCode(self):
        return self.incomeTypeCode

    def set_incomeTypeCode(self, value):
        self.incomeTypeCode = value

    def get_receiptDate(self):
        return self.receiptDate

    def set_receiptDate(self, value):
        self.receiptDate = value

    def get_filialCode(self):
        return self.filialCode

    def set_filialCode(self, value):
        self.filialCode = value

    def get_divisionId(self):
        return self.divisionId

    def set_divisionId(self, value):
        self.divisionId = value

    def get_increaseCorrespondentAccountDate(self):
        return self.increaseCorrespondentAccountDate

    def set_increaseCorrespondentAccountDate(self, value):
        self.increaseCorrespondentAccountDate = value

    def get_corAccountAmount(self):
        return self.corAccountAmount

    def set_corAccountAmount(self, value):
        self.corAccountAmount = value

    def get_corAccountCurrency(self):
        return self.corAccountCurrency

    def set_corAccountCurrency(self, value):
        self.corAccountCurrency = value

    def get_debitCorAccount(self):
        return self.debitCorAccount

    def set_debitCorAccount(self, value):
        self.debitCorAccount = value

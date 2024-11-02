from src.generated_data.bdvo.payment_bdvo_versions import Version


class MTCurrency(Version):
    def __init__(self, action, version):
        super().__init__(action, version)
        
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

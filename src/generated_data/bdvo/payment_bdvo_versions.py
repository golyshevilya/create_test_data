class Version:
    def __init__(self, action: str, version: str):
        self.action: str = action
        self.version: int = version
    
    def get_action(self):
        return self.action

    def set_action(self, value):
        self.action = value

    def get_version(self):
        return self.version

    def set_version(self, value):
        self.version = value

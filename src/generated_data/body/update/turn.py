from src.generated_data.body.abstract.versions import VersionAbstract


class TurnUpdate(VersionAbstract):
	def __init__(self, action, version):
		super().__init__(action, version)
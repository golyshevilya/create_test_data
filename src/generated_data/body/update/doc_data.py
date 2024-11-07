from src.generated_data.body.abstract.versions import VersionAbstract


class DocDataUpdate(VersionAbstract):
	def __init__(self, action, version):
		super().__init__(action, version)

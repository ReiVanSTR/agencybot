from typing import Dict, Optional, List

class Constructor:
	def __init__(self):
		self._data = {}
		print('Ok')

	def title(self, title: Dict[str, str], format: Optional[List[str]]) -> Dict[str, str]:
		self._data.update({'title':f"<b>{title['title']}</b>"})
		print(self._data["title"])
		return self._data["title"]


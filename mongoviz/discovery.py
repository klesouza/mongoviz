class Discovery():

	_collection = None
	def __init__(self, collection):
		self._collection = collection

	def list_collection_fields(self):
		item = self._collection.find({}, {"_id": 0})
		item.skip(100)
		return item.next().keys()

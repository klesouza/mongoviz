class AggregationBuilder:
    _collection = None
    _pipeline = []
    def __init__(self, col):
        self._collection = col

    def build(self, keyname, aggregation, aggfield = None, filter = None):
        group = {"$group": {"_id": "$"+keyname, "y": None}}
        if aggregation == 'count':
            group["$group"]["y"] = {"$sum": 1}
        elif aggregation == 'sum':
            if aggfield is None:
                raise 'The aggregation field must me selected'
            group["$group"]["y"] = {"$sum": "$"+aggfield}

        match = {"$match": {}}
        limit = {"$limit": 15}
        self._pipeline = [group, limit]

    def run(self, pipeline):
        return self._collection.aggregate(self._pipeline)

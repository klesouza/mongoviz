class AggregationBuilder:
    _collection = None
    _pipeline = []
    def __init__(self, col):
        self._collection = col

    def build(self, keyname, aggregation, aggfield = None, filter = None):
        group = {"$group": {"_id": "$"+keyname, "y": None}}
        if aggregation == 'count':
            group["$group"]["y"] = {"$sum": 1}
        elif aggregation in ['sum', 'avg']:
            if aggfield is None:
                raise 'The aggregation field must me selected'
            group["$group"]["y"] = {"$"+aggregation: "$"+aggfield}

        match = {"$match": {}}
        sort = {"$sort": {"_id": 1}}
        limit = {"$limit": 15}
        self._pipeline = [group,sort, limit]

    def parse_string(self, query):
        import json
<<<<<<< HEAD
        allowed = ["$match", "$group", "$unwind", "$sort", "$limit", "$project", "$redact", "$skip", "$geoNear"]
=======
        valid_operations = ["$match", "$group", "$limit", "$sort", "$unwind", "$project", "$skip", "$geoNear"]
>>>>>>> origin/master
        self._pipeline = json.loads(query)

    def run(self):
        return self._collection.aggregate(self._pipeline)

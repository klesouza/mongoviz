class AggregationBuilder:
    _collection = None
    _pipeline = []
    _result = None
    _errors = []
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
        allowed = ["$match", "$group", "$unwind", "$sort", "$limit", "$project", "$redact", "$skip", "$geoNear"]
        self._pipeline = json.loads(query)

    def has_errors(self):
        return len(self._errors) > 0

    def get_errors(self):
        return self._errors

    def validate_returning_fields(self):
        self._errors = []
        if len(self._result) == 0:
            return
        err = 'Your result must have "{}" field'
        if '_id' not in self._result[0]:
            self._errors.append(err.format('_id'))
        if 'y' not in self._result[0] and 'series' not in self._result[0]:
            self._errors.append(err.format('y or series'))
        if 'series' in self._result[0]:
            if not isinstance(self._result[0]['series'], list):
                self._errors.append('Your "series" must return an array')
            else:
                if len(self._result[0]['series']) > 0 and 'y' not in self._result[0]['series'][0]:
                    self._errors.append(err.format('series.y'))
                if len(self._result[0]['series']) > 0 and 'x' not in self._result[0]['series'][0]:
                    self._errors.append(err.format('series.x'))



    def run(self):
        self._result = [x for x in self._collection.aggregate(self._pipeline)]
        self.validate_returning_fields()
        return self._result

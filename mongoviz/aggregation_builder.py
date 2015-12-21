class AggregationBuilder:
    def __init__(self):
        pass
    @staticmethod
    def build(keyname, aggregation, aggfield = None, filter = None):
        group = {"$group": {"_id": "$"+keyname, "y": None}}
        if aggregation == 'count':
            group["$group"]["y"] = {"$sum": 1}
        elif aggregation == 'sum':
            if aggfield is None:
                raise 'The aggregation field must me selected'
            group["$group"]["y"] = {"$sum": "$"+aggfield}

        match = {"$match": {}}
        return [group]

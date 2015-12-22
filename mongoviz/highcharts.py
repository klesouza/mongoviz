class Highcharts:
    _chart = None
    _type = None
    LINE_TYPE = 'line'
    BAR_TYPE = 'bar'
    def __init__(self):
        self._chart = {
            "chart":{
                "type": "line"
            },
            "series": []
        }

    def set_charttype(self, type):
        self._type = type
        self._chart["chart"]["type"] = type

    def set_series(self, x, y):
        if self._type == LINE_TYPE:
            self._chart["series"] = [{
                "data": [[x[i], y[i]] for i in len(x)]
            }]
        if self._type == LINE_TYPE:
            self._chart["series"] = [{
                "data": [{"name": x[i], "y": y[i]} for i in len(x)]
            }]

    def choose_bestconfig(self, x, y):
        if isinstance(x[0], int):
            set_charttype(LINE_TYPE)
        elif isinstance(x[0], string):
            set_charttype(BAR_TYPE)
        set_series(x, y)
        return _chart

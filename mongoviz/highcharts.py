
LINE_TYPE = 'line'
BAR_TYPE = 'column'

class BaseChart(object):
    _chart = {}
    _data = None
    def __init__(self, data):
        self._data = data
        self._chart = {
            "chart":{
                "type": None
            },
            "tooltip": {
                "valueDecimals": 2
            },
            "series": []
        }
    def set_series(self):
        pass

class EmptyChart(BaseChart):
    def __init__(self):
        BaseChart.__init__(self, None)
    def set_series(self):
        pass

class LineChart(BaseChart):
    def __init__(self, data):
        BaseChart.__init__(self, data)
        self._chart["chart"]["type"] = LINE_TYPE
    def set_series(self):
        srt = sorted(self._data, key=lambda x: x['_id'])
        if any(( 'y' in x for x in self._data )):
            series = [{'name': x['name'], 'data': [srt[i], x['y']]} for i,x in enumerate([{'name': 'Default', 'y': srt}])]
        else:
            categories = [x['_id'] for x in srt]
            s = {}
            for m,d in enumerate(srt):
                for k in d["series"]:
                    if k["name"] not in s:
                        s[k['name']] = [0]*len(srt)
                    s[k['name']][m] = k['y']
            series = [{'name': x, 'data':y} for x,y in s.iteritems() ]
            self._chart["xAxis"] = {'categories': categories}
        self._chart["series"] = series

class BarChart(BaseChart):
    def __init__(self, data):
        BaseChart.__init__(self, data)
        self._chart["chart"]["type"] = BAR_TYPE

    def set_series(self):
        categories = [x['_id'] for x in self._data]
        if any(( 'y' in x for x in self._data )):
            series = [{'name': 'Default', 'data': [x['y'] for x in self._data ]}]
        else:
            s = {}
            for m,d in enumerate(self._data):
                for k in d["series"]:
                    if k["x"] not in s:
                        s[k['x']] = [0]*len(self._data)
                    s[k['x']][m] = k['y']
            series = [{'name': x, 'data':y} for x,y in s.iteritems() ]
        self._chart["xAxis"] = {'categories': categories}
        self._chart["series"] = series

class Chart:
    _current = None
    def __init__(self, data):
        _current = EmptyChart()
        print len(data)
        if isinstance(data,list) and len(data) > 0 and isinstance(data[0], dict) and '_id' in data[0]:
            if all([unicode(x['_id']).replace('.','').isdigit() for x in data]):
                self._current = LineChart(data)
            else:
                self._current = BarChart(data)
        self._current.set_series()

    def chart(self):
        return self._current._chart

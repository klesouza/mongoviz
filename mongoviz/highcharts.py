
LINE_TYPE = 'line'
BAR_TYPE = 'column'
import numpy as np
def set_charttype(_chart, _type):
    _chart["chart"]["type"] = _type

def set_series(_chart, _type, x, y, series):
    if _type == LINE_TYPE:
        _chart["series"] = [{
            "name": s,
            "data": [[xv, yv] for xv,yv in zip(np.sort(x[idx]), np.array(y[idx])[np.argsort(x[idx])])]
        } for idx, s in enumerate(series)]
    elif _type == BAR_TYPE:
        _chart["xAxis"] = {"categories": list(set(reduce(lambda a,b:a+b, x)))}
        _chart["series"] = [{"name": s, "data": y[idx]} for idx, s in enumerate(series)]

def choose_bestconfig(data):
    series = ["Default"]
    if 'y' in data[0]:
        x = [[d['_id'] for d in data]]
        y = [[d['y'] for d in data]]
    elif 'series' in data[0]:
        x = [[d['x'] for d in s['series']] for s in data]
        y = [[d['y'] for d in s['series']] for s in data]
        series = [d['_id'] for d in data]
    _chart = {
        "chart":{
            "type": LINE_TYPE
        },
        "tooltip": {
            "valueDecimals": 2
        },
        "series": []
    }
    _type = None
    i = 0
    while i < len(x) and x[i] is None:
        i += 1
    #grouped X
    if x[i] is not None and unicode(x[i][0]).isdigit():
        _type = LINE_TYPE
    else:# isinstance(x[0], str):
        _type = BAR_TYPE

    set_charttype(_chart, _type)
    set_series(_chart, _type, x, y, series)
    return _chart

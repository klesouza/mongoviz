
LINE_TYPE = 'line'
BAR_TYPE = 'column'

def set_charttype(_chart, _type):
    _chart["chart"]["type"] = _type

def set_series(_chart, _type, x, y):
    if _type == LINE_TYPE:
        _chart["series"] = [{
            "data": [[x[i], y[i]] for i in range(len(x))]
        }]
    elif _type == BAR_TYPE:
        _chart["xAxis"] = {"categories": x}
        _chart["series"] = [{"name": "Serie", "data": y}]

def choose_bestconfig(x, y):
    _chart = {
        "chart":{
            "type": "line"
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
    if x[i] is not None and unicode(x[i]).isdigit():
        _type = LINE_TYPE
    else:# isinstance(x[0], str):
        _type = BAR_TYPE

    set_charttype(_chart, _type)
    set_series(_chart, _type, x, y)
    return _chart

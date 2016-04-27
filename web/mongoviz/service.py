from flask import Flask, jsonify, request, make_response
from mongoviz import app, discovery
from mongoviz.discovery import Discovery
from mongoviz.aggregation_builder import AggregationBuilder
from mongoviz import highcharts
from pymongo import MongoClient
import json, os
from bson import json_util

def error_message(msg):
    return msg

@app.route('/')
@app.route('/<db>/<collection>', defaults={'db': None, 'collection': None})
def index(db = None, collection = None):
    appdir = os.path.abspath(os.path.dirname(__file__))
    return make_response(open(os.path.join(appdir, 'views/index.html')).read())

def getCollection(server, port, db, collection):
    try:
        client = MongoClient("mongodb://{}:{}/{}".format(server, port, db))
    except:
        raise ValueError('Please check your server configuration')
    #if db not in client.database_names():
    #   raise ValueError('This database does not exist')
    #if collection not in client[db].collection_names():
    #   raise ValueError('This collection does not exist')
    return client[db][collection]

@app.route('/<server>/<port>/<db>/<collection>')
def data(server, port, db, collection):
    try:
        col = getCollection(server, port, db, collection)
    except ValueError as e:
        return error_message(e)
    discovery = Discovery(col)
    return json.dumps({ 'fields': [x for x in discovery.list_collection_fields()]}, default=json_util.default)

@app.route('/<server>/<port>/<db>/<collection>/plot', methods=['POST'])
def plot(server, port, db, collection):
    col = getCollection(server, port, db, collection)
    data = json.loads(request.data)
    agg = AggregationBuilder(col)
    if data["selectedTab"] == 2:
        agg.build(data['selectedField'], data['selectedAgg'], data['selectedAggField'], data['selectedFilter'])
    elif data["selectedTab"] == 1:
        agg.parse_string(data['freeQuery'])
    else:
        raise 'Invalid request'

    result = agg.run()
    print result
    if agg.has_errors():
        return json.dumps(agg.get_errors(), default=json_util.default), 400
    from highcharts import Chart
    chart = Chart(result).chart()
    return json.dumps(chart, default=json_util.default)

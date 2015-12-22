from flask import Flask, jsonify, request, make_response
from mongoviz import app, discovery
from mongoviz.discovery import Discovery
from mongoviz.aggregation_builder import AggregationBuilder
from mongoviz import highcharts
from pymongo import MongoClient
import json
from bson import json_util

def error_message(msg):
	return msg

@app.route('/')
def index():
	return make_response(open('mongoviz/views/index.html').read())

def getCollection(server, port, db, collection):
	try:
		client = MongoClient(server, int(port))
	except:
		return error_message('Please check your server configuration')
	#print(help(client))
	if db not in client.database_names():
		return error_message('This database does not exist')
	if collection not in client[db].collection_names():
		return error_message('This collection does not exist')
	return client[db][collection]

@app.route('/<server>/<port>/<db>/<collection>')
def data(server, port, db, collection):
	col = getCollection(server, port, db, collection)
	discovery = Discovery(col)
	return json.dumps({ 'fields': [{'Id': x, 'Name': x} for x in discovery.list_collection_fields()]}, default=json_util.default)

@app.route('/<server>/<port>/<db>/<collection>/plot', methods=['POST'])
def plot(server, port, db, collection):
	col = getCollection(server, port, db, collection)
	data = json.loads(request.data)
	agg = AggregationBuilder(col)
	agg.build(data['selectedField']['Id'], data['selectedAgg'])
	data = [[x["_id"], x['y']] for x in agg.run()]
	app.logger.info(data)
	chart = highcharts.choose_bestconfig([x[0] for x in data], [x[1] for x in data])
	return json.dumps(chart, default=json_util.default)

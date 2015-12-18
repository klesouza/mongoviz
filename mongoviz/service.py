from flask import Flask, jsonify, request, make_response
from mongoviz import app, discovery
from pymongo import MongoClient

def error_message(msg):
	return msg

@app.route('/')
def index():
	return make_response(open('mongoviz/views/index.html').read())

@app.route('/<server>/<port>/<db>/<collection>')
def data(server, port, db, collection):
	try:
		client = MongoClient(server, port)
	except:
		return error_message('Please check your server configuration')
	if db not in client.getDatabaseNames():
		return error_message('This database does not exist')
	if collection not in client[db].collection_names(): 
		return error_message('This collection does not exist')
	
	discovery = Discovery(client[db][collection])
	return json.dumps({ 'fields': discovery.list_collection_names()}, default=json_util.default)
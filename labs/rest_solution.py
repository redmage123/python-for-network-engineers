#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

    
class Battles(Resource):

    def __init__(self):
        with open ('battles.csv') as f:
            self.data = f.read()

    def get(self,battle_name):
        for line in self.data:
            if battle_name in line.strip().split(',')[0]:
                return jsonify(line)

class Predictions(Resource):

    def __init__(self):

        with open ('character-predictions.csv') as f:
            self.data = f.read()

    def get(self):
        for line in self.data:
            if character_name in line.strip().split(',')[5]:
                return jsonify(line)

class Deaths(Resource):

    def __init__(self):
        with open ('character-deaths.csv') as f:
            self.data = f.read()

    def get(self,character_name ):
        for line in self.data:
            if character_name in line.strip().split(',')[0]:
                return jsonify(line)




api.add_resource(Battles, '/battles/<battle_name>') # Route_1
api.add_resource(Predictions, '/characters/predictions/<character_name>') # Route_2
api.add_resource(Deaths, '/characters/deaths/<character_name>') # Route_3


if __name__ == '__main__':
    app.run(port='5002')
                          

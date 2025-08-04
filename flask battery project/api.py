from flask_restful import Resource
from flask import jsonify
from store import generatecolloqialnumber, datefunction, subtractnumber, batteries

BATTERY_STORE = [
    {"battery_id": "100", "battery_type": "temp", "battery_temperature": "42"},
    {"battery_id": "200", "battery_type": "temp", "battery_temperature": "55"},
    {"battery_id": "300", "battery_type": "temp", "battery_temperature": "33"},
    {"battery_id": "100", "battery_type": "temp", "battery_temperature": "44"},
    {"battery_id": "100", "battery_type": "temp", "battery_temperature": "45"},
    {"battery_id": "200", "battery_type": "temp", "battery_temperature": "42"},
    {"battery_id": "200", "battery_type": "temp", "battery_temperature": "48"},
]

class Add(Resource):
    def get(self, userinput, userinput2):
        return jsonify(generatecolloqialnumber(userinput, userinput2))

class GrabDate(Resource):
    def get(self):
        return jsonify(datefunction())

class Subtract(Resource):
    def get(self, number1, number2):
        return jsonify(subtractnumber(number1, number2))

class GrabBattery(Resource):
    def get(self, battery_id):
        findmatch = [battery for battery in BATTERY_STORE if battery["battery_id"] == battery_id]
        if findmatch:
            return jsonify(findmatch)
        else:
            return "404"

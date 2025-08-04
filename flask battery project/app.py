from flask import Flask
from flask_restful import Api
from api import Add, GrabDate, Subtract, GrabBattery

app = Flask(__name__)
api = Api(app)

api.add_resource(Add, "/num/<int:userinput>_<int:userinput2>")
api.add_resource(GrabDate, "/date")
api.add_resource(Subtract, "/<int:number1>&<int:number2>")
api.add_resource(GrabBattery, "/api/batteries/<string:battery_id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


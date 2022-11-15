from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import random
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)


class PlotData(Resource):
    def get(self):
        return random.random()


api.add_resource(PlotData, '/plot')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import time
import subprocess
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
api = Api(app)
CORS(app)



class PlotData(Resource):
    def get(self):
        data = pd.read_csv('sensor_data.csv')
        return int(data['Distance'].iat[-1])


api.add_resource(PlotData, '/plot')

if __name__ == '__main__':
    subprocess.Popen(['py', '../main.py'])
    time.sleep(2)
    app.run(debug=True)

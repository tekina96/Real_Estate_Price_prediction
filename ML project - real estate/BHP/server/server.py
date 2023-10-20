from flask import Flask, request, jsonify
import util
from flask_cors import CORS
# from waitress import serve
app = Flask(__name__)
CORS(app)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    util.load_saved_artifact()
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # util.load_saved_artifact()
    # util.get_location_names()
    # util.get_estimated_price('1st Phase JP Nagar', )
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting the flask server for prediction")
    # serve(app, port=5000, host="127.0.0.1")
    util.load_saved_artifact()
    app.run()

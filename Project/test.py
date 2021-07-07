import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/api', methods=['POST'])
def predict():
    """
    docstring
    """
#     receive data from user
    data = request.get_json(force=True)
#     preprocessing
    data_to_score = data['exp']
#     inference
    prediction = model.predict(data_to_score)
#     postprocessing
    output = prediction.astype(int).tolist()
#     send data to user
    return jsonify(output)



@app.route('/',methods=['get'])
def hello_word():
    
    return 'PRIVET MOI dorAgoi DRUG!!!'


if __name__ == '__main__':
    app.run(port=8100, debug=True)

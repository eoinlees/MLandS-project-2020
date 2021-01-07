# flask for web app.
import numpy as np
import flask as fl
from flask import jsonify
# import keras load model
from tensorflow.keras.models import load_model
# Create a new web app.
app = fl.Flask(__name__, static_url_path='', static_folder='static')

# Load keras model from file
model = load_model('./my_model.h5')

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index.html')

# Add prediction route.
@app.route('/api/predict/<int:x>', methods=['GET'])
@app.route('/api/predict/<float:x>', methods=['GET'])
def predict(x):
    
    prediction = model.predict([x])
    answer = str(prediction[0][0])
    return {"value": answer}
    

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)

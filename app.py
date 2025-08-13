from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'insurancemodelf (2).pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker_input = request.form['smoker']

        # Encode 'smoker' feature
        smoker = 1 if smoker_input.lower() == 'yes' else 0

        # Prepare final input for prediction
        final_features = np.array([[age, bmi, children, smoker]])
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Predicted Insurance Price: ${output}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)

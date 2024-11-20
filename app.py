from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import math

app = Flask(__name__)

# Enable CORS for all domains (if you want to restrict it, replace '*' with the frontend domain)
CORS(app, origins=["*"])  # Or use: CORS(app, origins=["https://your-frontend-domain.com"])

def calculate_emi(principal, rate, tenure):
    # EMI calculation logic
    monthly_rate = rate / (12 * 100)
    emi = principal * monthly_rate * (math.pow(1 + monthly_rate, tenure)) / (math.pow(1 + monthly_rate, tenure) - 1)
    return round(emi, 2)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    principal = float(data.get('principal', 0))
    rate = float(data.get('rate', 0))
    tenure = int(data.get('tenure', 0)) * 12  # Convert years to months

    # Validate input
    if principal <= 0 or rate <= 0 or tenure <= 0:
        return jsonify({"error": "Invalid input values"}), 400

    emi = calculate_emi(principal, rate, tenure)
    return jsonify({"emi": emi})

if __name__ == '__main__':
    app.run(debug=True)

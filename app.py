import os
from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def calculate_emi(principal, rate, tenure):
    monthly_rate = rate / (12 * 100)
    emi = principal * monthly_rate * (math.pow(1 + monthly_rate, tenure)) / (math.pow(1 + monthly_rate, tenure) - 1)
    return round(emi, 2)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    principal = float(data.get('principal', 0))
    rate = float(data.get('rate', 0))
    tenure = int(data.get('tenure', 0)) * 12

    if principal <= 0 or rate <= 0 or tenure <= 0:
        return jsonify({"error": "Invalid input values"}), 400

    emi = calculate_emi(principal, rate, tenure)
    return jsonify({"emi": emi})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

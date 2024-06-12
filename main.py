
# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schemes', methods=['POST'])
def schemes():
    income_level = request.form['income_level']
    schemes = get_schemes(income_level)  # Implement this function to fetch schemes based on income level
    return render_template('schemes.html', schemes=schemes)

@app.route('/schemes/<scheme_id>')
def scheme_details(scheme_id):
    scheme = get_scheme_details(scheme_id)  # Implement this function to fetch details for a specific scheme
    return render_template('scheme_details.html', scheme=scheme)

if __name__ == '__main__':
    app.run(debug=True)

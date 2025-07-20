# Import classes and functions, and create a flask object 
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Define the home age route and render the html index 
@app.route('/')
def home():
    return render_template('index.html')

# Bank statement processing 
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'bankstatement' not in request.files:
        return "No file uploaded!"
    
    file = request.files['bankstatement']

    if file.filename == '':
        return "No file selected!"
    
    return f"You uploaded: {file.filename}" 
# 
if __name__ ==  '__main__':
    app.run(debug=True)
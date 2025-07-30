#TODO: refactor into OOP for finished product 
# Imports
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

#Create flask object
app = Flask(__name__)

# Define the home age route and render the html index 
@app.route('/')
def home():
    return render_template('index.html')

# Bank statement upload 
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'bankstatement' not in request.files:
        return "No file uploaded!"
    
    file = request.files['bankstatement']

    if file.filename == '':
        return "No file selected!"
    
    # Read bank statement 
    try:
        df = pd.read_csv(file)

        # Select columns to show
        statement_columns = ['Date', 'Description', 'Value', 'Balance']
        df_selected = df[statement_columns]

        #  TODO: Added for prototype - move HTML to proper template later
        return f"""
        <h2> File uploaded successfully: {file.filename} </h2>
        <p> Number of transactions: {len(df_selected)} </p>
        <p> Columns: {', ' .join(df.columns.tolist())} </p>
        <h3>First 5 rows:</h3>
        {df_selected.head().to_html()}
        """
    except Exception as e:
        return f"Error reading CSV file: {e}"
    
if __name__ ==  '__main__':
    app.run(debug=True)
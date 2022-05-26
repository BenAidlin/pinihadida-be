from flask import Flask, jsonify
from itsdangerous import json
import os

app = Flask(__name__)

def generate_html(message):
    html = """
        <html>
        <body>
            <div style='text-align:center;font-size:80px;'>
                <image height="340" width="1200" src="./extensions/hadida-logo.jpg">
                <br>
                <p>Coming soon...</p>
                <br>
            </div>
        </body>
        </html>"""
    return html

def greet():
    greeting = 'Welcome to CI/CD'
    return greeting

@app.route('/')
def hello_world():
    html = generate_html(greet())
    return html
@app.route('/json')
def return_json():
    response = {"one":1,"two":2}
    return jsonify(response)
    
if __name__ == '__main__':
    app.run()
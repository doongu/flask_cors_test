from flask import Flask , redirect, url_for, request, render_template, jsonify, make_response
from flask_cors import CORS, cross_origin
app = Flask(__name__)

@app.route('/', methods=["GET", "OPTIONS"])
def api_create_order():
    _build_cors_preflight_response()
    return render_template("index.html")

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

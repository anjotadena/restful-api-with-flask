from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users/ping', methods=['GET'])
def user_ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


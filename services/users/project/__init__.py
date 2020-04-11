from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def user_ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


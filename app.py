from flask import Flask

app = Flask(__name__)

print(f"__name__ = {__name__}")

@app.route('/')
def home():
    return "Hello, World!"

# GET - used to receive data
# POST - used to store data

@app.route('/stores', methods=['POST'])
def create_store():
    pass

@app.route('/stores/<string:name>')
def get_store(name):
    pass

@app.route('/stores')
def get_stores():
    pass

@app.route('/stores/<string:name>/items', methods=['POST'])
def create_stores_item():
    pass

app.run(port=5000)

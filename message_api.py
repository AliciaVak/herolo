from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/write_msg', methods=['POST'])
def write_msg():
    pass


@app.route('/api/get_all_msg', methods=['GET'])
def get_all_msg():
    pass


@app.route('/api/get_all_unread_msg', methods=['POST'])
def get_all_unread_msg():
    pass


@app.route('/api/read_msg', methods=['POST'])
def read_msg():
    pass


@app.route('/api/delete_msg', methods=['POST'])
def delete_msg():
    pass
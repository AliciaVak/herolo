from flask import Flask, request, jsonify
import datetime
import db_api
import json


app = Flask(__name__)


@app.route('/api/write_msg', methods=['POST'])
def write_msg():
    msg_arguments = json.loads(request.get_data())
    creation_date = str(datetime.datetime.now())
    db_api.add_msg(msg_arguments, creation_date)
    return jsonify({})


@app.route('/api/get_all_msg', methods=['GET'])
def get_all_msg():
    arguments = json.loads(request.get_data())
    user = arguments["user"]
    user_msgs = db_api.get_all_user_msgs(user)
    return jsonify(user_msgs)


@app.route('/api/get_all_unread_msg', methods=['GET'])
def get_all_unread_msg():
    arguments = json.loads(request.get_data())
    user = arguments["user"]
    user_unread_msgs = db_api.get_all_user_unread_msgs(user)
    return jsonify(user_unread_msgs)


@app.route('/api/read_msg', methods=['POST'])
def read_msg():
    arguments = json.loads(request.get_data())
    user = arguments["user"]
    msg_id = arguments["message_id"]
    msg = db_api.read_msg(user, msg_id)
    return jsonify(msg)


@app.route('/api/delete_msg', methods=['POST'])
def delete_msg():
    arguments = json.loads(request.get_data())
    user = arguments["user"]
    msg_id = arguments["message_id"]
    response = db_api.delete_msg(user, msg_id)
    return jsonify(response)


if __name__ == '__main__':
    app.run()



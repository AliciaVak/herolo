from pymongo import MongoClient
from bson import ObjectId

MONGO_URL = "mongodb+srv://dbMessages:8487@cluster0-gv270.mongodb.net/test?retryWrites=true&w=majority"

cluster = MongoClient(MONGO_URL)
db = cluster["messagesApp"]
collection = db["Messages"]


def add_msg(msg, creation_date):
    collection.insert_one({"sender": msg["sender"], "receiver": msg["receiver"],
                           "subject": msg["subject"], "message": msg["message"], "creation date": creation_date,
                           "read": "false"})


def get_all_user_msgs(user):
    msgs = []
    ret_msg = collection.find({"receiver": user})
    for m in ret_msg:
        msgs.append(parse_msg(m))
    return msgs


def get_all_user_unread_msgs(user):
    unread_msgs = []
    ret_msg = collection.find({"receiver": user, "read": "false"})
    for m in ret_msg:
        unread_msgs.append(parse_msg(m))
    return unread_msgs


def read_msg(user, msg_id):
    msg = collection.find_one({"_id": ObjectId(msg_id)})
    if msg:
        if msg["receiver"] == user:
            if msg["read"] == "false":
                collection.update_one({"_id": ObjectId(msg_id)}, {"$set": {"read": "true"}})
            return parse_msg(msg)
        if msg["sender"] == user: #
            return parse_msg(msg)
        return {"error": "The given user can't access this message"}

    return {"error": "Message not found"}


def delete_msg(user, msg_id):
    msg = collection.find_one({"_id": ObjectId(msg_id)})
    if msg:
        if msg["receiver"] == user or msg["sender"] == user:
            ret = collection.delete_one({"_id": msg_id})
            if ret:
                return "Message successfully deleted"

        return "The given user cant delete this message"

    return "Message not found"


def parse_msg(m):
    return {"msg_id": str(m["_id"]), "sender": m["sender"], "receiver": m["receiver"],
            "subject": m["subject"], "message": m["message"], "creation date": m["creation date"]}

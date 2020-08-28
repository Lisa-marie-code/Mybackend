from flask import Flask, jsonify, request
from flask_pymongo import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://flask:flask1234@covid19.z2ije.mongodb.net/PaseBlog?retryWrites=true&w=majority")

collection = client.PaseBlog.posts


# get all
@app.route("/blogs", methods=["GET"])
def get_blog():
    data = []
    for response in collection.find():
        data.append(
        {
            "_id": str(response["_id"]),
            "post": response["post"],
            "image": response["image"],
            "title": response["title"],
            "categories": response["categories"],
            "tags": response["tags"],
            "date": response["date"],
            "author": response["author"]
        }   
        )
    return jsonify(data)

# get one
@app.route("/blog/<id>", methods=["GET"])
def read_one(id):
    response = collection.find_one ({"_id": ObjectId(id)})
    if response:
        return jsonify(
            {
            "_id": str(response["_id"]),
            "post": response["post"],
            "image": response["image"],
            "title": response["title"],
            "categories": response["categories"],
            "tags": response["tags"],
            "date": response["date"],
            "author": response["author"]
            }
        )

#  post one  
@app.route("/blog", methods=["POST"])
def create_blog():
    collection.insert_one(
        {
            "post": request.json["post"],
            "image": request.json["image"],
            "title": request.json["title"],
            "categories": request.json["categories"],
            "tags": response["tags"]
            "date": request.json["date"],
            "author": request.json["author"], 
        }
    )
    return request.json 

# update blog
@app.route("/blog/<id>", methods=["PUT"])
def update_one(id):
    response = collection.find_one_and_update({"_id": ObjectId(id)}, {"$set":request.json})
    if response:
        return jsonify(
            {
            "_id": str(response["_id"]),
            "post": response["post"],
            "image": response["image"],
            "title": response["title"],
            "categories": response["categories"],
            "tags": response["tags"]
            "date": response["date"],
            "author": response["author"]
            }
        )

# delete blog
@app.route("/blog/<id>", methods=["DELETE"])
def delete_one(id):
    response = collection.find_one_and_delete({"_id": ObjectId(id)})
    if response:
        return jsonify(
            {
            "_id": str(response["_id"]),
            "post": response["post"],
            "image": response["image"],
            "title": response["title"],
            "categories": response["categories"],
            "tags": response["tags"]
            "date": response["date"],
            "author": response["author"]
            }
        )


if __name__ == "__main__":
    app.run(port=6077, debug=True)
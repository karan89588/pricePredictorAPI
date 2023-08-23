from flask import Flask, request, jsonify
from flask_pymongo import ObjectId
from pymongo import MongoClient
from flask_cors import CORS
import pythonScript

uri='mongodb+srv://karanmouryadmp:karan@cluster0.fzwllfy.mongodb.net/?retryWrites=true&w=majority'
client=MongoClient(uri,tls=True,tlsAllowInvalidCertificates=True)

appp=Flask(__name__)
CORS(app)

mydatabase=client['flaskcrud']
db=mydatabase['users']


@appp.route('/',methods=['GET'])
def get():
    return jsonify({'msg':'Hello'})

@appp.route('/users',methods=['GET'])
def getUsers():
    users=[]
    for doc in db.find():
        users.append({
            'state':doc['state'],
            'season':doc['season'],
            'name':doc['name'],
            'availability':doc['availability'],
            'demand':doc['demand'],
            'output':doc['output']
        })
        return jsonify(users)

@appp.route('/users',methods=['Put'])
def update():
    data=pythonScript.predictPrice(request.json['name'],request.json['season'],request.json['state'],request.json['availability'],request.json['demand'])
    db.update_one({'_id':ObjectId(request.json['id'])},{'$set':{
        'name':request.json['name'],
        'season':request.json['season'],
        'state':request.json['state'],
        'availability':request.json['availability'],
        'demand':request.json['demand'],
        'output':str(data)
    }})
    return jsonify({'msg':"updated"})

if __name__=='__main__':
    app.run(debug=True)

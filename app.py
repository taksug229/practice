from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'testdb'
app.config["MONGO_URI"] = "mongodb://localhost:27017/testdb"
mongo = PyMongo(app)
 
@app.route('/')
def get_all_titles():
  titles = mongo.db.titles
  output = []
  for s in titles.find():
    output.append({'title': s['title']})
  return jsonify({'result': output})


@app.route('/star', methods=['POST'])
def add_star():
  title = mongo.db.titles
  name = request.json['name']
  distance = request.json['distance']
  title_id = title.insert({'name': name, 'distance': distance})
  new_title = title.find_one({'_id': title_id})
  output = {'name': new_title['name'], 'distance': new_title['distance']}
  return jsonify({'result': output})
 
if __name__ == "__main__":
    app.run(debug=True)


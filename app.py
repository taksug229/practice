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


if __name__ == "__main__":
    app.run(debug=True)


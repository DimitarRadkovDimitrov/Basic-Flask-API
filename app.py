from flask import Flask, jsonify
import json 

app = Flask(__name__)

hard_coded_tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def hello():
    html = "<h1>Hello World!</h1>" 
    html = html + "<p> POST /api/tasks </p>"
    html = html + "<p> GET /api/tasks </p>"
    html = html + "<p> Example: </p>"
    html = html +  json.dumps(hard_coded_tasks[0])
    return html

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': hard_coded_tasks})

@app.route('/api/tasks', methods=['POST'])
def post_tasks():
    return jsonify({'status':'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

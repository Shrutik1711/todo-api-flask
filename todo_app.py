from dotenv import load_dotenv
import os
from flask import Flask , jsonify , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
load_dotenv()
db_password = os.getenv('DB_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://avnadmin:{db_password}@mysql-3207d3c7-shrutiknandeshwar-7333.k.aivencloud.com:10604/defaultdb"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer , primary_key= True)
    username = db.Column(db.String(100) , unique = True , nullable = False)
    password = db.Column(db.String(100) , nullable = False)

class Todo(db.Model):
    id = db.Column(db.Integer , primary_key= True)
    task = db.Column(db.String(100) , nullable = False)
    completed = db.Column(db.Boolean , default = False)  


with app.app_context():
    db.create_all()


@app.route("/signup" , methods=["POST"])
def signup():
    data = request.json
    new_user = User(username=data['username'] , password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message" :" user register succesfully !!!"})

@app.route("/login" , methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and user.password == data['password'] :
        return jsonify ({"message" : "Login succsfully !!"})
    else :
        return jsonify ({"message" : "Invaild username and password deatils  !!"}) , 401


@app.route("/todos" , methods=["POST"])
def add_todos():
    data = request.json
    new_todo = Todo(task=data['task'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify ({"message": "Todo added successfully!"})    

@app.route("/todos" , methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    result = [{"id" : t.id , "task" : t.task , "completed" : t.completed}for t in todos]
    return jsonify(result)


@app.route("/todos/<int:id>" , methods=["PUT"])
def update_todo(id):
    todo = Todo.query.get(id)
    if not todo :
        return jsonify({"message" : "todo was not found "}) ,404

    data = request.json
    todo.completed = data.get('completed' , todo.completed)
    db.session.commit()
    return jsonify ({"message" : "Todo updated succsfully !!"})


@app.route("/todos/<int:id>" , methods=["DELETE"])
def delete_todo(id):
    todo = Todo.query.get(id)
    if not todo :
        return jsonify({"message" : "todo was not found "}) ,404

    db.session.delete(todo)
    db.session.commit()
    return jsonify ({"message" : "Todo Deleted succsfully !!"})


if __name__  == '__main__':
    app.run(debug=True)


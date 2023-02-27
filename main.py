from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.name}>"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([user.__dict__ for user in users])

    elif request.method == 'POST':
        data = request.get_json()
        user = User(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.__dict__)

if __name__ == '__main__':
    app.run()
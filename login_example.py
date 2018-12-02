from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/sungurovae/flask_login/login_app/login.db'
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
	id=db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route('/')
def index():
	user = User.query.filter_by(username='sungurov').first()
	login_user(user)
	return 'You are now logged in !'

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return 'Вы вышли из системы!'

@app.route('/home')
@login_required
def home():
	return 'Текущий пользователь: ' + current_user.username


if __name__ == '__main__':
	app.run(debug=True)


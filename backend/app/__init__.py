from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager


db = SQLAlchemy()
io = SocketIO()
lm = LoginManager()


def create_app():
	
	app = Flask(__name__)
	
	app.config['SECRET_KEY'] = b".\x9b\xf1\x7f\x14\xb4\\\xae\xd7(t\xf5VUs\xd2\x91:\xa2\xc0l\xf3(p\x8b\x8c\x8b(\xdfJ\xce\x0b>?\x93~2\xcf\nAs_\x1a\xbe\x1bT\x87\xa1Fz\xf8\xa0\x9f\xc2\x8e\x8e{\x7fm\xfd\x15\xb4\xdb;2\xfc*\xe7%EO2b@\xa1oK\x03\xb2\xfa\xce\xde\xf0\xa3V\x0b\x85U\x1b\xcf\xf4\xf8`\xd5\x11'\x93\xc7\x07l"
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	# postgresql://username:password@host:port/database_name
	# mysql://username:password@host:port/database_name
	
	
	db.init_app(app)
	io.init_app(app)
	lm.init_app(app)
	
	with app.app_context():
		
		
		db.create_all()
		
		return app

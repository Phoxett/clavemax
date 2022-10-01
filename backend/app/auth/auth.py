from .. import lm
from .model import db


@lm.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
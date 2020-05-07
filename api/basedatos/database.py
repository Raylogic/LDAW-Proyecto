from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
def initialize_db(app):
    db.init_app(app)
    Migrate(app, db,compare_type=True)
    bcrypt.init_app(app)
from flask import Flask
from flask_login import (
    LoginManager,
)

from database import db
from models.user import User
from routes.auth import auth_bp
from routes.daily import daily_bp

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(auth_bp)
app.register_blueprint(daily_bp)


if __name__ == "__main__":
    app.run(debug=True)

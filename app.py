from flask import Flask

from models import db
from services import bcrypt
from controllers import jwt, auth_blueprint, blog_controller

app = Flask(__name__)

# Setting our configuration style
app.config.from_object('config.Development')

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Add blueprints here
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(blog_controller, url_prefix="/blog")


if __name__ == "__main__":
    app.run()
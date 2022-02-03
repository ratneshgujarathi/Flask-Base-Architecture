# Flask essentials


from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Flask_Base_Arch.config import base_config

# app declaration
app = Flask(__name__, template_folder='../resources/views/',
            static_folder='../static')
CORS(app)

# config for app
app.config.from_object(base_config.BaseConfig)

# db connection
db = SQLAlchemy(app)
from Flask_Base_Arch.app.models import _db

Migrate(app, _db)

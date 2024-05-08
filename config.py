import os
from dotenv import load_dotenv

load_dotenv()
# APP CONFIGURATIONS
HOST = os.environ.get("HOST", "localhost")
PORT = os.environ.get("PORT", "8000")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", True)
SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
ENV = os.environ.get("ENV", "production")
# DATABASE CONFIGURATIONS
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


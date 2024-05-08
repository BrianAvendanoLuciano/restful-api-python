from  extensions import db
from app import app
from sqlalchemy import text

sql = open("users.sql", "r")
statement = sql.read()

with app.app_context():
    db.session.execute(text(statement))
    db.session.commit()
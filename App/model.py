from App.ext import db


class example(db.Model):
    __tablename__ = "table_name"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(20))


class projectLog(db.Model):
    __tablename__ = "project_log"
    id = db.Column(db.Integer,primary_key=True)

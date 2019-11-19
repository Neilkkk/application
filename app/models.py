from app import db


class task (db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date)
    title = db.Column(db.String(250))
    description = db.Column(db.String(250))
    state = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.date + ' ' + self.title + ' ' + self.description + ' ' + self.state

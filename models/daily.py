from database import db


class Daily(db.Model):
    id: db.Column(db.Integer, primary_key=True)
    name: db.Column(db.String(100), nullable=False)
    description: db.Column(db.String(200))
    data_time: db.Column(db.DateTime, nullable=False)
    is_diet: db.Column(db.Boolean, default=False)

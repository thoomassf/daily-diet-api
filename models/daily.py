from database import db


class Daily(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    data_time = db.Column(db.DateTime, nullable=False)
    is_diet = db.Column(db.Boolean, default=False)
    user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def to_disc(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "data_time": self.data_time.strftime("%d/%m/%Y %H:%M"),
            "is_diet": self.is_diet,
            "user": self.user,
        }

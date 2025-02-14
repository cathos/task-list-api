from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable = False)
    tasks = db.relationship("Task", back_populates="goal")

    def to_dict(self):
        return {
            "id": self.goal_id,
            "title": self.title
            }

    def dict_with_tasks(self):
        return {
            "id": self.goal_id,
            "title": self.title,
            "tasks": self.tasks
        }
    
    def single_dict(self):
        return {
            "goal":self.to_dict()
        }
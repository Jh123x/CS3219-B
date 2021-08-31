from django.db import models

# Create your models here.
class TodoItems(models.Model):
    description = models.CharField(max_length=1000)
    is_completed = models.BooleanField(default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "is_completed": self.is_completed,
        }

    def __repr__(self) -> str:
        return f"TodoItem {self.id}: {self.description}. Status: {self.is_completed}"
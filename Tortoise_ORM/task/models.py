from tortoise import fields
from tortoise.models import Model


class Task(Model):
    task_id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=250)
    description = fields.TextField(null=True)

    #class Meta:
        #table = 'tasks'

    def __str__(self):
        return self.name
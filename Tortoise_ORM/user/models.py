from tortoise import fields, models
from tortoise.models import Model

class User(Model):
    user_id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=250)
    firstname = fields.CharField(max_length=250)
    lastname = fields.CharField(max_length=250)
    age = fields.IntField()


    def __str__(self):
        return self.username

from mongoengine import *
import datetime

connect('project2')

class User(Document):
    email = StringField(default="user")
    password = StringField(default="pass")
    key = StringField(default="")
    expiration = DateTimeField(default=datetime.datetime.now)

def updateKey(email, key):
    users = User.objects()
    for u in users:
        if u.email==email:
            u.update(set__key=str(key))
            u.update(set__expiration = datetime.datetime.now)
        else:
            pass

def changePassword(email, password):
    users = User.objects()
    for u in users:
        if u.email==email:
            u.update(set__password=str(password))
        else:
            pass


def retUsers():
    users = User.objects()
    for u in users:
        print (u.email + " " + u.key + " " + str(u.expiration))

kathy = User(email="Kathy")
kathy.save()
tbone = User(email="Theo")
tbone.save()
updateKey("Kathy", "oasbdoasdbvashdv")
retUsers()

from .DBConfig import engine
from blog.db.user.UserDao import createTableUser

def initAndCreateTable():
    createTableUser(engine)
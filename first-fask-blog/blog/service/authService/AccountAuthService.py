from . import AuthLoginAbstact
from blog.domain.user.LoginInfo import LoginInfo
from blog.db.user.UserDao import selectUser

class AccountAuthService(AuthLoginAbstact.AuthAbstract):

    @classmethod
    def check(cls, login: LoginInfo):
        user = selectUser(login.username)
        if user is None:
            return False
        elif user.password != login.pwd:
            return False
        else: return True


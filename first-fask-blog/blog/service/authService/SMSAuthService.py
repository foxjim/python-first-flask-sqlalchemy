from . import AuthLoginAbstact
from blog.domain.user.LoginInfo import LoginInfo


class SMSAuthService(AuthLoginAbstact.AuthAbstract):

    @classmethod
    def check(cls, login: LoginInfo):
        print("SMSAuthService.check")
        if login.status == '1':
            return True
        else: return False

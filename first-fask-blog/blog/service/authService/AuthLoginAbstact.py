from blog.domain.user.LoginInfo import LoginInfo
import abc


class AuthAbstract(metaclass=abc.ABCMeta):
    """抽象鉴权类"""

    @abc.abstractmethod
    def check(self: LoginInfo):
       pass
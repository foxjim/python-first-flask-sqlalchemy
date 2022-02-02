from enum import Enum


class GrandType(Enum):
    """登陆类型枚举类"""
    # 账号密码模式
    GrandType_PWD = 'password',

    # 短信验证码模式
    GrandType_SMS = 'sms',

    # 邮箱登陆
    GrandType_EMAIL = 'email';

    def valueStr(self):
        return self.value[0]
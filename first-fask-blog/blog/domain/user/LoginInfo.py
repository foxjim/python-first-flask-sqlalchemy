from ..enum.GrandTypeEnum import GrandType
from blog.domain.exception.auth.AuthInitException import AuthInitException


class LoginInfo:
    """用户登陆类"""
    # 登陆类型
    grand_type = '';

    # 用户名
    username = '';

    # 密码
    pwd = ''

    # 登陆状态 0-失败 1-成功
    status = 0

    def __init__(self):
        pass

    def __init__(self, params={}):
        self.initParams(params)

    def initParams(self, params={}):
        if "sta" in params :
            self.status = params['sta']

        print(params)
        if not ('grand_type' in params):
            raise AuthInitException("未知请求")
        else:
            grandType = params['grand_type']
            self.grand_type = grandType

            if grandType == GrandType.GrandType_PWD.value[0]:
                if 'name' in params:
                    self.username = params['name']
                else:
                    raise AuthInitException('账号或密码未输入')
                if 'pwd' in params:
                    self.pwd = params['pwd']
                else:
                    raise AuthInitException('账号或密码未输入')
            elif grandType == GrandType.GrandType_EMAIL.value[0]:
                raise AuthInitException('不受支持的登陆方式')
            elif grandType == GrandType.GrandType_SMS.value[0]:
                raise AuthInitException('不受支持的登陆方式')
            else:
                raise AuthInitException('不受支持的登陆方式')

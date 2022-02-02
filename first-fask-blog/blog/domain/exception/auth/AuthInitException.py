
class AuthInitException(Exception):
    """初始化异常"""

    value = None

    def __init__(self, value):
        self.value = value
        # 返回异常类对象的说明信息

    def __str__(self):
        return "{} is invalid input".format(repr(self.value))
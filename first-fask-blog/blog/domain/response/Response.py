from blog.domain.enum.HttpCodeEnum import HttpCodeEnum


class ResponseCommon:
    code = ''
    msg = ''
    data = None

    def __int__(self):
        pass

    def __init__(self, code, msg):
        self.code = code;
        self.msg = msg;

    def __init__(self, code, msg, data):
        self.code = code;
        self.msg = msg;
        self.data = data;

    def toJsonStr(self):
        return self.__dict__

    @staticmethod
    def success(msg):
        return ResponseCommon(HttpCodeEnum.HTTP_200.valueStr(), msg);

    @staticmethod
    def success(msg, data):
        return ResponseCommon(HttpCodeEnum.HTTP_200.valueStr(), msg, data);

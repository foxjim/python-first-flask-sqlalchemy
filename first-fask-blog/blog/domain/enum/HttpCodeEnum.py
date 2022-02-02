from enum import Enum


class HttpCodeEnum(Enum):
    """网络返回值"""
    HTTP_200 = '200',
    HTTP_400 = '400',
    HTTP_500 = '500',
    HTTP_PARAMS_EMPTY = '1000',
    HTTP_PARAMS_TYPE_ERROR = '1001';

    def valueStr(self):
        return self.value[0]

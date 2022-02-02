from flask import Blueprint, jsonify
from flask import request
from blog.domain.user.LoginInfo import LoginInfo
from blog.domain.exception.auth.AuthInitException import AuthInitException
from blog.domain.response.Response import ResponseCommon
from blog.domain.enum.HttpCodeEnum import HttpCodeEnum
from blog.domain.enum.GrandTypeEnum import GrandType
from blog.service.authService.AccountAuthService import AccountAuthService
from blog.service.authService.SMSAuthService import SMSAuthService

authLogin = Blueprint('authLogin', __name__)


@authLogin.route("/v1/token", methods=['GET'])
def auth():
    try:
        info = LoginInfo(request.args);
        # return jsonify(ResponseCommon.success('请求成功', info.__dict__).toJsonStr());
        if info.grand_type == GrandType.GrandType_PWD.valueStr():
            # 账号密码模式
            if AccountAuthService.check(info):
                return jsonify(ResponseCommon.success('登陆成功', info.__dict__).toJsonStr())
            else:
                return jsonify(ResponseCommon(HttpCodeEnum.HTTP_500.valueStr(), '登陆失败，账号或密码错误', None).toJsonStr())
        elif info.grand_type == GrandType.GrandType_SMS.valueStr():
            # 短信验证码模式
            if SMSAuthService.check(info):
                return jsonify(ResponseCommon.success('登陆成功', info.__dict__).toJsonStr())
            else:
                return jsonify(ResponseCommon(HttpCodeEnum.HTTP_500.valueStr(), '登陆失败，账号或密码错误', None).toJsonStr())
        elif info.grand_type == GrandType.GrandType_EMAIL.valueStr():
            # 邮箱登陆模式
            return jsonify(ResponseCommon(HttpCodeEnum.HTTP_PARAMS_TYPE_ERROR.valueStr(), '暂不支持的登陆方式', None).toJsonStr())
        else:
            return jsonify(ResponseCommon(HttpCodeEnum.HTTP_PARAMS_TYPE_ERROR.valueStr(), '未知登陆方式', None).toJsonStr())

    except AuthInitException as e:
        return jsonify(ResponseCommon(HttpCodeEnum.HTTP_500.valueStr(), e.value, None).toJsonStr());

from flask import Blueprint, jsonify
from flask import request

user = Blueprint('user', __name__)


@user.route("/api/v1", methods=['GET', 'POST'])
def mainApp0v1():
    if request.method == "POST":
        return QueryNamev1()
    else:
        return jsonify({"code": 0, "data": "get方法干啥呢"})


def QueryNamev1():
    data = "我是测试app01项目-api.v1版本"
    return jsonify({"code": 0, "data": "post方法干啥呢"})

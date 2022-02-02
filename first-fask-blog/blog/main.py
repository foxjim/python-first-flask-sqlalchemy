from flask import Flask
from view.auth.authLoginController import authLogin
from view.user.user import user
from blog.db.DBInit import initAndCreateTable

app = Flask(__name__)


# 鉴权模块
app.register_blueprint(authLogin, url_prefix='/authLogin')

# 用户模块
app.register_blueprint(user, url_prefix='/user')
app.config["JSON_AS_ASCII"] = False

if __name__ == '__main__':
    print("initAndCreateTable")
    initAndCreateTable()
    app.run()

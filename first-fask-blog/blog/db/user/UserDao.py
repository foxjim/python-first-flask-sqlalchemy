from sqlalchemy import Column, VARCHAR, DateTime, Integer
import datetime
from sqlalchemy.ext.declarative import declarative_base
from blog.db.DBConfig import DBSession

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 't_user'

    # 表的结构:
    userid = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False, comment="主键Id")
    username = Column(VARCHAR(64), nullable=False, comment="姓名")
    loginname = Column(VARCHAR(64), nullable=False, comment="登陆名", unique=True)
    password = Column(VARCHAR(128), nullable=False, comment="密码")
    phone = Column(VARCHAR(16), nullable=True, comment="电话号码")
    email = Column(VARCHAR(255), nullable=True, comment="邮箱地址")
    role = Column(VARCHAR(128), nullable=False, comment="角色，用逗号隔开")
    status = Column(VARCHAR(1), nullable=False, default="0", comment=" 状态 0-正常  1-删除（default 0）")
    remarks = Column(VARCHAR(512), nullable=True, comment=" 描述")
    createtime = Column(DateTime, nullable=False, default=datetime.datetime.now, comment=" 账号创建时间")
    lastmodifytime = Column(DateTime, nullable=False, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now, comment=" 最后一次修改时间")
    createuser = Column(VARCHAR(64), nullable=True, comment=" 创建人")
    lastmodifyuser = Column(VARCHAR(64), nullable=True, comment=" 最后一次修改人")


def createTableUser(engine):
    # 创建表
    Base.metadata.create_all(engine)
    print("创建表t_user")


def selectUser(loginName):
    session = DBSession();
    user = session.query(User).filter(User.loginname == loginName).first();
    session.close()  # 关闭Session
    return user

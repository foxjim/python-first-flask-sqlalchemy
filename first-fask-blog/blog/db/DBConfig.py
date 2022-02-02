from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine('postgres://bzd:123456@121.5.100.120:8832/py_blog')  # 用户名:密码@localhost:端口/数据库名

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)



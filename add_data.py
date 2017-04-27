# -*- coding：utf-8 -*-


from blog import db
from blog.models import User, Role, Article, Category

title = '解决Flask-SQLAlchemy中文乱码问题'
des = '发现查询到的结果显示乱码 。这里将解决方法记录下'
text = '''
![Top_image](/static/img/top_image1.png "Top_image")

一、问题

这两天在学习使用flask + SQLAlchemy 定制一个web查询页面的demo ，在测试时，发现查询到的结果显示乱码 。这里将解决方法记录下。

二、解决思路

1、flask 程序上定位

flask的文档中提到可以通过设置SQLALCHEMY_NATIVE_UNICODE来禁止使用SQLAlchemy默认的Unicode编码。有可能是SQLAlchemy默认的Unicode编码不是UTF-8，抱着这样的想法，在程序中指定了“SQLALCHEMY_NATIVE_UNICODE=False”，执行程序，报错。

flask中还提到“use_native_unicode”为目标编码来指定编码方式，尝试将“db = SQLAlchemy(app)”改为“db = SQLAlchemy(app, use_native_unicode=”utf8″)”。这回虽然没报错，但还是乱码。

2、mysql 上定位

突然想到有可能是建表的时候，没有指定字符集，使用的是数据库默认的字符集的导致的。继续找了一段时间的如何指定建表时使用字符集的方法，未果。

数据库该不会使用的不是UTF-8吧？抱着这个想法，进入数据库，输入“status”，在输出的信息上显示默认是latin-1。搞了半天，原来问题在这。

mysql> status
--------------
mysql  Ver 14.14 Distrib 5.1.73, for redhat-linux-gnu (x86_64) using readline 5.1
Connection id:          9
Current database:      web12306
Current user:           root@localhost
SSL:                    Not in use
Current pager:          stdout
Using outfile:          ''
Using delimiter:        ;
Server version:         5.1.73 Source distribution
Protocol version:       10
Connection:             Localhost via UNIX socket
Server characterset:    utf8
Db     characterset:    utf8
Client characterset:    latin1
Conn.  characterset:    latin1
UNIX socket:            /var/lib/mysql/mysql.sock
3、解决问题

即然找到了，问题就在mysql 的my.cnf 上增加相关配置，并重启mysql 服务：

# 进入mysql的配置文件目录
cd /etc/mysql/
# 编辑my.cnf配置文件
vim my.cnf
# 在文件中的[mysqld]下面增加一行内容
character_set_server = utf8
# 在[client]和[mysql]下面分别增加一行内容
default-character-set = utf8
# 保存。然后重启MySQL的服务，设置就生效了
service mysqld restart
注：需要注意的是，之前已经存在的数据，在上面修改过后，通过mysql select查询时会是乱码，需要重新导入。'''


class Add(object):

    def add_admin_role(self):
        admin_role = Role(role='Admin')
        db.session.add(admin_role)
        db.session.commit()
        return

    def add_user(self):
        admin_role = Role.query.filter_by(role='Admin').first()
        user1 = User(name='Admin1', role=admin_role)
        user1.password = '111111'
        db.session.add(user1)
        db.session.commit()
        return

    def add_category(self):
        new = Category(name='Python')
        db.session.add(new)
        db.session.commit()

    def add_articles(self, count=1):
        user = User.query.filter_by(name='Admin1').first()
        cate = Category.query.filter_by(name='Python').first()
        for i in range(count):
            art = Article(title='(%s)%s' % (i, title), description=des, text=text, user=user, category=cate)
            db.session.add(art)
        db.session.commit()

    def start(self, count=1):
        self.add_admin_role()
        self.add_user()
        self.add_category()
        self.add_category(count)

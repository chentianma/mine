# -*- coding：utf-8 -*-


from blog import db
from blog.models import User, Role, Article, Category

title = '解决Flask-SQLAlchemy中文乱码问题'
des = '解决问题;Flask;SQLAlchemy;中文乱码'
text = '''

![Top_image](/static/img/top_image1.png "Top_image")

## 一、问题

这两天在学习使用flask + SQLAlchemy 定制一个web查询页面的demo ，在测试时，发现查询到的结果显示乱码 。这里将解决方法记录下。

## 二、解决思路

### ***1、flask 程序上定位***
flask的文档中提到可以通过设置SQLALCHEMY_NATIVE_UNICODE来禁止使用SQLAlchemy默认的Unicode编码。有可能是SQLAlchemy默认的Unicode编码不是UTF-8，抱着这样的想法，在程序中指定了“SQLALCHEMY_NATIVE_UNICODE=False”，执行程序，报错。

flask中还提到“use_native_unicode”为目标编码来指定编码方式，尝试将“db = SQLAlchemy(app)”改为“db = SQLAlchemy(app, use_native_unicode=”utf8″)”。这回虽然没报错，但还是乱码。

 ### ***2、mysql 上定位***

突然想到有可能是建表的时候，没有指定字符集，使用的是数据库默认的字符集的导致的。继续找了一段时间的如何指定建表时使用字符集的方法，未果。

数据库该不会使用的不是UTF-8吧？抱着这个想法，进入数据库，输入“status”，在输出的信息上显示默认是latin-1。搞了半天，原来问题在这。
>
 <link rel='stylesheet' type='text/css' href='http://tools.oschina.net/js/syntaxhighlighter_3.0.83/styles/shCoreEclipse.css'/><div id="highlighter_724035" class="syntaxhighlighter  xml"><div class="toolbar"><span><a href="#" class="toolbar_item command_help help">?</a></span></div><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div><div class="line number3 index2 alt2">3</div><div class="line number4 index3 alt1">4</div><div class="line number5 index4 alt2">5</div><div class="line number6 index5 alt1">6</div><div class="line number7 index6 alt2">7</div><div class="line number8 index7 alt1">8</div><div class="line number9 index8 alt2">9</div><div class="line number10 index9 alt1">10</div><div class="line number11 index10 alt2">11</div><div class="line number12 index11 alt1">12</div><div class="line number13 index12 alt2">13</div><div class="line number14 index13 alt1">14</div><div class="line number15 index14 alt2">15</div><div class="line number16 index15 alt1">16</div><div class="line number17 index16 alt2">17</div><div class="line number18 index17 alt1">18</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="xml plain">mysql&gt;&nbsp;status</code></div><div class="line number2 index1 alt1"><code class="xml plain">--------------</code></div><div class="line number3 index2 alt2"><code class="xml plain">mysql&nbsp;&nbsp;Ver&nbsp;14.14&nbsp;Distrib&nbsp;5.1.73,&nbsp;for&nbsp;redhat-linux-gnu&nbsp;(x86_64)&nbsp;using&nbsp;readline&nbsp;5.1</code></div><div class="line number4 index3 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Connection&nbsp;id:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9</code></div><div class="line number5 index4 alt2"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Current&nbsp;database:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;web12306</code></div><div class="line number6 index5 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Current&nbsp;user:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root@localhost</code></div><div class="line number7 index6 alt2"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">SSL:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Not&nbsp;in&nbsp;use</code></div><div class="line number8 index7 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Current&nbsp;pager:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stdout</code></div><div class="line number9 index8 alt2"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Using&nbsp;outfile:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;''</code></div><div class="line number10 index9 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Using&nbsp;delimiter:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;;</code></div><div class="line number11 index10 alt2"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Server&nbsp;version:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.1.73&nbsp;Source&nbsp;distribution</code></div><div class="line number12 index11 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Protocol&nbsp;version:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10</code></div><div class="line number13 index12 alt2"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Connection:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localhost&nbsp;via&nbsp;UNIX&nbsp;socket</code></div><div class="line number14 index13 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Server&nbsp;characterset:&nbsp;&nbsp;&nbsp;&nbsp;utf8</code></div><div class="line number15 index14 alt2"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Db&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;characterset:&nbsp;&nbsp;&nbsp;&nbsp;utf8</code></div><div class="line number16 index15 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Client&nbsp;characterset:&nbsp;&nbsp;&nbsp;&nbsp;latin1</code></div><div class="line number17 index16 alt2"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">Conn.&nbsp;&nbsp;characterset:&nbsp;&nbsp;&nbsp;&nbsp;latin1</code></div><div class="line number18 index17 alt1"><code class="xml spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="xml plain">UNIX&nbsp;socket:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/var/lib/mysql/mysql.sock</code></div></div></td></tr></tbody></table></div>

### ***3、解决问题***

即然找到了，问题就在mysql 的my.cnf 上增加相关配置，并重启mysql 服务：

* ### 进入mysql的配置文件目录

>		cd /etc/mysql/

* ### 编辑my.cnf配置文件

>		vim my.cnf

* ### 在文件中的[mysqld]下面增加一行内容

>		character_set_server = utf8

* ### 在[client]和[mysql]下面分别增加一行内容

>		default-character-set = utf8

* ### 保存。然后重启MySQL的服务，设置就生效了

>		service mysqld restart

**注：**需要注意的是，之前已经存在的数据，在上面修改过后，通过*mysql select*查询时会是乱码，需要重新导入。'''


class Add(object):

    def add_admin_role(self):
        admin_role = Role(role='Admin')
        db.session.add(admin_role)
        db.session.commit()
        return

    def add_user(self):
        admin_role = Role.query.filter_by(role='Admin').first()
        user1 = User(name='admin', role=admin_role)
        user1.password = '3322505'
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
        self.add_articles(count)

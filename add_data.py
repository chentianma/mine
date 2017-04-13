# -*- coding：utf-8 -*-


from blog import db
from blog.models import User, Role, Article, Category

title = 'JSON格式的字符串|Something about JSON'
des = 'JSON是JavaScript Object Notation的缩写，它是一种数据交换格式。'
text = '''
## JSON
----

![Top_image](/static/img/top_image1.png "Top_image")

>在JSON出现之前点击，大家一直用XML来传递数据。
    ---- [Baidu](http://www.baidu.com/ "Baidu")


    class Article(db.Model):

        __tablename__ = 'Article'

        id = db.Column(db.Integer, primary_key=True)
        img = db.Column(db.String(100))
        title = db.Column(db.String(100))
        description = db.Column(db.String(90))
        text = db.Column(db.Text)
        pub_date = db.Column(db.DateTime, default=datetime.utcnow())
        author_id = db.Column(db.Integer, db.ForeignKey('User.id'))
        category_id = db.Column(db.Integer, db.ForeignKey('Category.id')

        def __repr__(self):
            return '<Article %r>' % self.title

   终于，在2002年的一天，道格拉斯·克罗克福特（Douglas Crockford）同学为了拯救深陷水深火热同时又被某几个巨型软件企业长期愚弄的软件工程师，发明了JSON这种超轻量级的数据交换格式。

道格拉斯同学长期担任雅虎的高级架构师，自然钟情于JavaScript。他设计的JSON实际上是JavaScript的一个子集。

----
>#### 在JSON中，一共就这么几种数据类型：

>>##### number：和JavaScript的number完全一致；
>>##### boolean：就是JavaScript的true或false  [百度一下](http://www.baidu.com/ "Baidu")
>>##### string：就是JavaScript的string；
>>##### null：就是JavaScript的null；
>>##### array：就是JavaScript的Array表示方式——[]；
>>##### object：就是JavaScript的{ ... }表示方式。

>#### 以及上面的任意组合。

****
* 并且，JSON还定死了字符集必须是UTF-8，表示多语言就没有问题了。为了统一解析，JSON的字符串规定必须用双引号""，Object的键也必须用双引号""[百度一下](http://www.baidu.com/ "Baidu")。

* 由于JSON非常简单，很快就风靡Web世界，并且成为ECMA标准。几乎所有编程语言都有解析JSON的库，而在JavaScript中，我们可以直接使用JSON，因为JavaScript内置了JSON的解析。

* 把任何JavaScript对象变成JSON，就是把这个对象序列化成一个JSON格式的字符串，这样才能够通过网络传递给其他计算机。

如果我们收到一个JSON格式的字符串，只需要把它反序列化成一个JavaScript对象，就可以在JavaScript中直接使用这个对象了。
'''


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


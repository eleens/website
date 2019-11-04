# _*_ coding:utf-8 _*_

"""
#=============================================================================
#  ProjectName: website
#     FileName: models
#         Desc: 
#       Author: yutingting
#        Email:
#     HomePage:
#       Create: 2019-04-28 22:53
#=============================================================================
"""
from mysite import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    # description = db.Column(db.Text)

    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.ForeignKey(User.id), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.current_timestamp())
    author = db.relationship(User, lazy="joined", backref="posts")


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                       doc="标签ID")
    tag_name = db.Column(db.String, nullable=False, doc="标签名称")
    tag_description = db.Column(db.Text, nullable=True, doc="标签描述")


class PostTag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column(db.ForeignKey(Tag.id), nullable=False)
    post_id = db.Column(db.ForeignKey(Post.id), nullable=False)
    posts = db.relationship(Post, lazy="joined", backref="post_tag")
    tags = db.relationship(Tag, lazy="joined", backref="post_tag")


class Sort(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                        doc="分类ID")
    sort_name = db.Column(db.String, nullable=False, doc="分类名称")
    sort_description = db.Column(db.Text, nullable=True, doc="分类描述")
    # parent_sort_id = db.Column(db.BIGINT, nullable=False)


class PostSort(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sort_id = db.Column(db.ForeignKey(Sort.id), nullable=False)
    post_id = db.Column(db.ForeignKey(Post.id), nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                           doc="评论ID")

    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.current_timestamp())
    comment_user = db.Column(db.String, nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.ForeignKey(Post.id), nullable=False)
    post = db.relationship(Post, lazy="joined", backref="comments")

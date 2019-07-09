# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:18
"""
from mysite.blog_duane import mod
from mysite.databases.models import Post, User
from flask import render_template


@mod.route('/')
def blog():
    posts = Post.query.join(User).filter_by(username='duane').all()
    return render_template('blog/qearl.html', blog_list=posts)
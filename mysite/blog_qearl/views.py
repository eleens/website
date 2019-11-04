# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:19
"""
from mysite.blog_qearl import mod
from mysite import db
from mysite.databases.models import Post, User, Tag, Sort, PostTag
from flask import render_template, request, g, redirect, url_for, flash
from mysite.auth.views import login_required


@mod.route('/')
def blog():
    posts = Post.query.join(User).filter_by(username='qearl').all()
    return render_template('blog/list.html', blog_list=posts)


# @mod.route('/<int:blog_id>')
# def show(blog_id):
#     posts = Post.query.join(User).filter_by(username='qearl').all()
#     post = Post.query.filter_by(id=blog_id).join(PostTag).first()
#     return render_template('blog/show.html', blog=post, blog_list=posts)













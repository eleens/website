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
from mysite.databases.models import Post, User
from flask import render_template, request, g, redirect, url_for, flash
from mysite.auth.views import login_required


@mod.route('/')
def blog():
    posts = Post.query.join(User).filter_by(username='qearl').all()
    return render_template('blog/qearl.html', blog_list=posts)


@mod.route('/<int:blog_id>')
def show(blog_id):
    posts = Post.query.join(User).filter_by(username='qearl').all()
    post = Post.query.filter_by(id=blog_id).join(User).filter_by(username='qearl').first()
    return render_template('blog/show.html', blog=post, blog_list=posts)


@mod.route('/create', methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        error = None

        if not title:
            error = "请输入标题"
        elif not text:
            error = "请输入内容"

        if error is None:
            db.session.add(Post(title=title, body=text, author=g.user))
            db.session.commit()
            return redirect(url_for('qearl.blog'))
        flash(error)
    return render_template('blog/create.html')


@mod.route('/<int:blog_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_id):
    post = Post.query.get(blog_id)
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        error = None

        if not title:
            error = "请输入标题"
        elif not text:
            error = "请输入内容"

        if error is None:
            post.title = title
            post.body = text
            db.session.commit()
            return redirect(url_for("qearl.blog"))
        flash(error)
    return render_template("blog/show.html", post=post)










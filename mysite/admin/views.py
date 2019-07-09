# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:18
"""
from mysite import db
from mysite.admin import mod
from mysite.databases.models import Post, User, Tag, Sort, PostTag, PostSort
from mysite.auth.views import login_required
from flask import render_template, request, g, redirect, url_for, flash


@mod.route('/overview/<string:username>')
def blog(username):
    posts = Post.query.join(User).filter_by(username=username).all()
    return render_template('admin/blog.html', blog_list=posts)

@mod.route('/blog/create', methods=["GET", "POST"])
@login_required
def create_blog():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        tags = request.form.get("tag", "")
        sort = request.form.get("sort")
        tags = tags.split(",")
        error = None

        if not title:
            error = "请输入标题"
        elif not text:
            error = "请输入内容"

        if error is None:
            post_obj = Post(title=title, body=text, author=g.user)
            db.session.add(post_obj)
            db.session.flush()
            for tag in tags:
                tag_obj = Tag.query.filter_by(tag_name=tag).first()
                if not tag_obj:
                    tag_obj = Tag(tag_name=tag)
                    db.session.add(tag_obj)
                    db.session.flush()
                db.session.add(PostTag(tag_id=tag_obj.id, post_id=post_obj.id))
            db.session.commit()
            return redirect(url_for('admin.blog', username=g.user.username))
        flash(error)
    return render_template('admin/create.html')


@mod.route('/blog/<int:blog_id>/update', methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    post = Post.query.get(blog_id)
    tag = Tag.query.join(PostTag).filter_by(post_id=blog_id).all()
    sort = Sort.query.join(PostSort).filter_by(post_id=blog_id).all()
    tags = [t.tag_name for t in tag]
    sorts = [t.sort_name for t in sort]
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
            return redirect(url_for("admin.blog", username=g.user.username))
        flash(error)
    return render_template("admin/update.html", post=post, tags=tags, sorts=sorts)

#
# @mod.route('/blog/<int:blog_id>/delete', methods=['GET', 'POST'])
# def delete_blog(blog_id):
#     post = Post.query.get(blog_id)
#     if request.method == "POST":
#         db.session.remove(post)
#         db.session.commit()
#     return redirect(url_for('admin.blog'))
#
#
# @mod.route('/tag/create', method=['GET', 'POST'])
# def create_tag():
#     if request.method == "POST":
#         tag = request.form.get("tag")
#         des = request.form.get("description")
#         error = None
#         if not tag:
#             error = "请输入标签"
#         if error is None:
#             db.session.add(Tag(tag_name=tag, tag_description=des))
#             db.session.commit()
#             redirect(url_for('admin.tag'))
#     return render_template('blog/create.html')



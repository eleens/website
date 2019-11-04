# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:19
"""
from mysite.blog import mod
from mysite import db
from sqlalchemy import func, and_
from mysite.databases.models import Post, User, Tag, Sort, PostTag, PostSort
from flask import render_template, request, g, redirect, url_for, flash
from mysite.auth.views import login_required


@mod.route('/<string:username>')
def blog(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.join(User).filter_by(username=username).all()
    tags = db.session.query(Tag.tag_name, func.count('*').label('tag_count')
                            ).filter(
        and_(Tag.id == PostTag.tag_id, PostTag.post_id == Post.id,
             PostTag.post_id == Post.id, Post.author_id == User.id,
             User.username == username)).group_by(Tag.tag_name).all()
    sorts = db.session.query(Sort.sort_name, func.count('*').label('sort_count')
                             ).filter(
        and_(Sort.id == PostSort.sort_id, PostSort.post_id == Post.id,
             User.username == username)).group_by(
        Sort.sort_name).all()
    return render_template('blog/list.html', blog_list=posts, user=user,
                           tags=tags, sorts=sorts)


@mod.route('/<string:username>/<int:blog_id>')
def show(username, blog_id):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.join(User).filter_by(username=username).all()
    post = Post.query.filter_by(id=blog_id).join(PostTag).first()
    index = posts.index(post)
    post_pre = posts[index - 1] if index > 0 else None
    post_next = posts[index + 1] if index < len(posts) - 1 else None
    return render_template('blog/show.html', blog=post, blog_list=posts,
                           user=user, post_pre=post_pre, post_next=post_next)

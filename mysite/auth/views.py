# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:13
"""
import functools
from flask import request, session, redirect, url_for, flash, render_template, g
from werkzeug.security import check_password_hash, generate_password_hash
from mysite.auth import mod

from mysite import db
from mysite.databases.models import User


@mod.route('/register', methods=["GET", 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username:
            error = "用户名或密码不能为空"
        elif not password:
            error = "密码不能为空"
        elif db.session.query(
            User.query.filter_by(username=username).exists()
        ).scalar():
            error = "用户名已经存在"

        if error is None:
            db.session.add(User(username=username,
                                password=generate_password_hash(password)))
            db.session.commit()
            return redirect(url_for("auth.login"))

        flash(error)
    return render_template("auth/register.html")


@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        # 从数据库获取
        user = User.query.filter_by(username=username).first()
        if not user:
            error = "用户不存在"
        elif not check_password_hash(user.password, password):
            error = "密码不正确"

        if error is None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')


@mod.route('/logout')
def logout():
    """退出登录"""
    session.clear()
    return redirect(url_for('index'))


@mod.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    user = User.query.get(user_id) if user_id else None
    g.user = user


def login_required(view):
    @functools.wraps(view)
    def wrap_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrap_view





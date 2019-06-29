# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:11
"""
import os

import click
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext

db = SQLAlchemy()


def create_app(test_config=None):
    # 创建和配置app
    app = Flask(__name__, instance_relative_config=True)

    # 从环境变量中获取db路径
    db_url = os.environ.get("DATABASE_URL")

    if db_url is None:
        db_url = "sqlite:///" + os.path.join(app.instance_path, "website.sqlite")
        os.makedirs(app.instance_path, exist_ok=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=db_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    # 加载配置
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # 注册各种模块到app
    from mysite import auth
    from mysite import dashboard
    from mysite import blog_qearl
    # from mysite import blog_duane
    # from mysite import abouts

    Bootstrap(app)
    db.init_app(app)
    app.cli.add_command(init_db_command)

    app.register_blueprint(auth.mod)
    app.register_blueprint(dashboard.mod)
    # app.register_blueprint(blog_duane.mod)
    app.register_blueprint(blog_qearl.mod)
    # app.register_blueprint(abouts.mod)
    app.add_url_rule('/', endpoint='index')

    return app


def init_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

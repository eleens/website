# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:13
"""
from flask import Blueprint

mod = Blueprint('auth', __name__, url_prefix='/auth')

from . import views
# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:13
"""
from flask import Blueprint

mod = Blueprint('abouts', __name__, url_prefix='/abouts')

from . import views
# _*_ coding:utf-8 _*_

"""
Description:
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午5:17
"""
from flask import Blueprint

mod = Blueprint('qearl', __name__, url_prefix='/qearl')

from . import views


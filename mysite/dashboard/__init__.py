# _*_ coding:utf-8 _*_

"""
#=============================================================================
#  ProjectName: website
#     FileName: __init__
#         Desc: 
#       Author: yutingting
#        Email:
#     HomePage:
#       Create: 2019-04-29 10:35
#=============================================================================
"""

from flask import Blueprint

mod = Blueprint('dashboard', __name__)

from . import views
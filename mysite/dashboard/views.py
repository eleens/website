# _*_ coding:utf-8 _*_

"""
#=============================================================================
#  ProjectName: website
#     FileName: view
#         Desc: 
#       Author: yutingting
#        Email:
#     HomePage:
#       Create: 2019-04-29 10:35
#=============================================================================
"""
from flask import render_template
from mysite.dashboard import mod


@mod.route('/')
def index():
    # return 'Hello World!'
    return render_template('index.html')

# _*_ coding:utf-8 _*_

"""
#=============================================================================
#  ProjectName: website
#     FileName: filter
#         Desc: 
#       Author: yutingting
#        Email:
#     HomePage:
#       Create: 2019-07-02 13:46
#=============================================================================
"""
from datetime import datetime


@app.template_filter()
def format_date(date):
    return datetime.strptime(date, "%Y年%M月%D日")
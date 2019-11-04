# _*_ coding:utf-8 _*_

"""
Description:The endpoint to start the project.
Author:qearl
HomePage:
Email:
Date: 2018/10/21: 下午4:59
"""
from mysite import create_app


app = create_app()


@app.template_filter("datafomat")
def datafomat(value, format="%Y-%m"):
    return value.strftime(format)


if __name__ == '__main__':

    app.run()

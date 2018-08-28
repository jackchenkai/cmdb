#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import uuid
import os

from tornado.options import define,options,parse_command_line
define("port",default=8888,help="run on the given port",type=int)

# 定义路由配置
handlers = [
	(r"/",MainHandler),
	(r"/login",LoginHandler),
	(r"/logout",LogoutHandler),
]
# 定义参数配置
settings = dict(
	template_path = os.path.join(os.path.dirname(__file__),"templates"), # 主服务脚本相对目录 模块文件夹
	static_path =  os.path.join(os.path.dirname(__file__),"static"), # 主服务脚本相对目录 静态资源文件夹
	cookie_secret = "justdoit", # 安全cookie机制的 密钥
	xsrf_cookies = True, # 开启防止跨站攻击
	debug = True, # 开启调试模式，方便查错，该代码，自动重启服务
	login_url=  "/login", # 设置登录url
	)

application = tornaro.web.Application(handlers,**settings)


def main():
	# 解析命令参数
	parse_command_line()
	# 监听运行程序时，传入的端口
	application.listen(options.port)
	# 挂起运行

	try:
		tornado.ioloop.IOLoop.instance().start()
	except KeyboardInterrupt:
		tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__name__":
	main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import string
import tornado.web
import tornado.ioloop
import tornado.escape
import tornado.options
import tornado.httpserver
from Handlers.APIHandler import CommonAPIHandler
from Handlers.MainHandler import MainHandler
from Handlers.BaseHandler import BaseHandler
from tools.arduino import Arduino

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# app's title
__title__ = 'Arduino@Home'

tornado.options.define("port", default=8080, help="run on the given port", type=int)

arduino = Arduino()


def generate_cookie_secrets(cookies_nb: int = 1, cookies_len: int = 128):
    cookie_secrets = {}
    if cookies_nb > 0:
        for i in range(cookies_nb - 1):
            cookie_secrets[i] = ''.join([random.choice(string.printable) for _ in range(cookies_len)])
    return cookie_secrets


class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            'static_path': './static',
            'template_path': './templates',
            'cookie_secret': generate_cookie_secrets(10, 1024),
            'login_url': '/auth/login',
            'xsrf_cookies': True,
        }
        # create an app instance
        handlers = [
            (r'/', MainHandler),  # index.html
            (r'/api(.*)$', CommonAPIHandler, {'arduino': arduino}),
            (r'/.*', BaseHandler),
        ]
        super(Application, self).__init__(handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    print("Server Listen {}".format(tornado.options.options.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()

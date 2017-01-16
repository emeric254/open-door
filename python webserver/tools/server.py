# -*- coding: utf-8 -*-

import sys
import tornado.httpserver
import tornado.ioloop
import tornado.netutil
import tornado.process
import tornado.web


def start_http(app: tornado.web.Application, http_port: int = 80):
    """Create app instance(s) binding a port.

    :param app: the app to execute in server instances
    :param http_port: port to bind
    """
    # HTTP socket
    http_socket = tornado.netutil.bind_sockets(http_port)
    #
    # try to create threads
    try:
        tornado.process.fork_processes(0)  # fork
    except KeyboardInterrupt:  # except KeyboardInterrupt to "properly" exit
        tornado.ioloop.IOLoop.current().stop()
    except AttributeError:  # OS without fork() support ...
        print('Can\' fork, continuing with only one (the main) thread ...', file=sys.stderr)
        pass  # don't fork and continue without multi-threading
    #
    # bind http port
    print('Start an HTTP request handler on port : ' + str(http_port))
    tornado.httpserver.HTTPServer(app).add_sockets(http_socket)
    #
    # loop forever to satisfy user's requests, except KeyboardInterrupt to "properly" exit
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()

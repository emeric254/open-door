# -*- coding: utf-8 -*-

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """Superclass for Handlers which require a connected user
    """

    def get_current_user(self):
        """Get current connected user
        :return: current connected user
        """
        return self.get_secure_cookie("user")

    def get(self):
        self.set_status(404)
        self.render('404.html')
        return

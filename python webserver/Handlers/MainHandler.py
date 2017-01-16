# -*- coding: utf-8 -*-

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """Handle '/' endpoint (root server endpoint).
    """

    def get(self):
        """Handle GET requests. Serve the index web page.
        """
        self.render('index.html')
        return

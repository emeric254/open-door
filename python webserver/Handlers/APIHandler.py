# -*- coding: utf-8 -*-

import random
import tornado.web
import tornado.escape


class CommonAPIHandler(tornado.web.RequestHandler):
    """Class to handle '/api' endpoint.
    """

    def initialize(self, arduino):
        self.arduino = arduino

    def get(self, path_request):
        """Handle GET requests.

        :param path_request: request path ( < URI)
        """
        if path_request == '/random':
            self.write(str(random.randint(0, 100)))
        else:
            self.send_error(status_code=400, reason='bad request')

    def post(self, path_request):
        """Handle POST requests.

        :param path_request: request path ( < URI)
        """
        if path_request.startswith('/open'):
            if path_request == '/open/door':
                self.arduino.send_msg('open door')
                self.arduino.wait_answer('opening door')
                self.write({'statusText': 'door opened'})
                return
            elif path_request == '/open/fence':
                return self.send_error(501)
                # self.arduino.send_msg('open fence')
                # self.arduino.wait_answer('opening fence')
                # self.write({'statusText': 'fence opened'})
                # return
        self.send_error(status_code=400, reason='bad request')
        return

from flask import url_for
from xunta import create_app


class BaseSuite(object):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def url_for(self, *args, **kwargs):
        with self.app.test_request_context():
            return url_for(*args, **kwargs)
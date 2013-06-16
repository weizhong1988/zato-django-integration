from zato.client import AnyServiceInvoker

class ZatoMiddleware(object):
    def process_request(self, req):
        req.zato_client = AnyServiceInvoker('http://localhost:17010', 
            '/django/sample', ('django-app', 'django-password'))
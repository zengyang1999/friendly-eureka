import time

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class TimeItMiddleware(MiddlewareMixin):
    def process_request(self,request):
        return
    def process_view(self,request,funs,*args,**kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response=funs(request)
        costed=time.time()-start
        print('process view: {:.2f}s'.format(costed))
        return response
    def process_exception(self,request,exception):
    def process_template_response(self,request,response):
        return response
    def process_response(self,request,response):
        return response
from .models import Request


class RequestMiddleware(object):

    def process_request(self, request):
        new_http = Request(
            http_inf='http://' + request.get_host() + request.META['PATH_INFO']
        )
        new_http.save()

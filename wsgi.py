from wsgiref.simple_server import make_server
from urlparse import parse_qs
from ask import wsgi


def parse_params(params):
    res = ''
    for p in params:
        for v in params[p]:
            res = res + p + '=' + v + '\n'
    return res


def app(environ, start_response):
    query = environ['QUERY_STRING']
    params = query
    if query is not '':
        params = parse_qs(query, True, True)
    res = parse_params(params)
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return res

httpd = make_server('', 8000, wsgi.application)
print("Serving on port 8000...")
httpd.serve_forever()

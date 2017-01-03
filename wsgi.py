from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def parse_params(params):
    res = ''
    for p in params:
        for v in params[p]:
            res = res + p + '=' + v + '\n'
    return res


def app(environ, start_response):
    query = environ['QUERY_STRING']
    params = parse_qs(query, strict_parsing=True)
    res = parse_params(params)
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [res.encode()]

httpd = make_server('', 8000, app)
print("Serving on port 8000...")
httpd.serve_forever()

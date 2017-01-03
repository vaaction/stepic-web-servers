from urlparse import parse_qs


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
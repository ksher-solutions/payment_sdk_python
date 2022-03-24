from collections import namedtuple

_apiType = namedtuple('API_TYPE', 'REDIRECT CSCANB FINANCE')
API_TYPE = _apiType('/redirect','/cscanb','/finance')
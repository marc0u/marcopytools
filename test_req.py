from marcotools import req

# r = req.get("http://httpstat.us/200?sleep=3000", tries=4, delay=1, backoff=2, timeout=(2, 2), jitter=(1, 2))

print(req.get('https://httpbin.org/get'))
print(req.post('https://httpbin.org/post'))
print(req.put('https://httpbin.org/put'))
print(req.patch('https://httpbin.org/patch'))
print(req.delete('https://httpbin.org/delete'))
print(req.options('https://httpbin.org/options'))
print(req.head('https://httpbin.org/head'))
